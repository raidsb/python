import os.path as osp
import os
import shutil
from typing import Callable, List, Optional

from torch_geometric.data import (
    Data,
    InMemoryDataset,
    download_url,
    extract_zip,
    extract_gz,
    extract_tar
)

import torch

class NeuroGraphDataset(InMemoryDataset):
    url = 'https://www.nitrc.org/frs/downloadlink.php/9066'
    filenames = {
        'ABIDE_2_BNI': 'ABIDEII-BNI_1.tar.gz'
    }

    def __init__(
            self,
            root: str,
            name: str,
            transform: Optional[Callable] = None,
            pre_transform: Optional[Callable] = None,
            pre_filter: Optional[Callable] = None,
    ):
        assert name in self.filenames.keys()
        self.name = name

        # super().__init__(root, transform, pre_transform, pre_filter)
        # self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def raw_dir(self) -> str:
        return os.path.join(self.root, self.name, 'raw')

    @property
    def raw_file_names(self) -> str:
        return 'ds.data'

    @property
    def processed_dir(self) -> str:
        return os.path.join(self.root, self.name, 'processed')

    @property
    def processed_file_names(self) -> str:
        return 'ds.data'

    def download(self):
        # url = f'{self.url}/{self.filenames[self.name]}'
        url = f'{self.url}'
        path = download_url(url, self.raw_dir)
        # extract_zip(path, self.raw_dir)
        extract_gz(path, self.raw_dir)
        path_tar = path[:-2]
        extract_tar(path_tar, self.raw_dir)
        os.unlink(path)
        os.unlink(path_tar)
        os.rename(
            osp.join(self.raw_dir, self.name, 'processed', f'{self.name}.data'),
            osp.join(self.raw_dir, 'data.pt'))
        shutil.rmtree(osp.join(self.raw_dir, self.name))

    def process(self):
        import os
        # data, slices = torch.load(self.raw_paths[0])
        data_list = ["ABIDE\\ABIDEII-BNI_1\\ABIDEII-BNI_1\\29006", "ABIDE\\ABIDEII-BNI_1\\ABIDEII-BNI_1\\29007"]
        for l in data_list:
            os.chmod(l, 0o777)
        data, slices = torch.load(data_list[0])

        num_samples = slices['x'].size(0) - 1
        data_list: List[Data] = []
        for i in range(num_samples):
            x = data.x[slices['x'][i]:slices['x'][i + 1]]
            edge_index = data.edge_index[
                         :,
                         slices['edge_index'][i]:slices['edge_index'][i + 1],
                         ]
            sample = Data(x=x, edge_index=edge_index, y=data.y[i])

            if self.pre_filter is not None and not self.pre_filter(sample):
                continue

            if self.pre_transform is not None:
                sample = self.pre_transform(sample)

            data_list.append(sample)
        data, slices = self.collate(data_list)
        torch.save((data, slices), self.processed_paths[0])

if __name__ == '__main__':
    my_own_ds = NeuroGraphDataset("ABIDE\\downloaded","ABIDE_2_BNI")
    # my_own_ds.download()
    my_own_ds.process()
    print("ds length, ", my_own_ds.len())
