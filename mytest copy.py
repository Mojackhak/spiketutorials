#%%
import os
import spikeinterface.full as si
from spikeinterface.extractors import toy_example
from spikeinterface.sorters import run_sorter
wd = r"F:\GitHub\anipose_m\Mojackhak\spiketutorials\test"
os.chdir(wd)
si.available_sorters()
# si.installed_sorters()
# ironclust
#%%
recording, _ = toy_example(
    duration=30,
    seed=0,
    num_channels=64,
    num_segments=1
)
# recording = recording.save(folder=r"F:\GitHub\anipose_m\Mojackhak\spiketutorials\test\test-docker-folder", overwrite=True)

#%%
sorting_TDC = run_sorter(sorter_name="tridesclous", recording=recording, detect_threshold=4)
print(sorting_TDC)

# %%
sorting_SC2 = run_sorter(sorter_name="spykingcircus2", recording=recording)

# %%
sorting_KS2 = run_sorter(sorter_name="kilosort2", recording=recording, 
                         installation_mode='pypi',
                         docker_image=True, verbose=True)
# %%
sorting_SC2 = run_sorter(sorter_name="spykingcircus2", recording=recording)


#%%
run_sorter(sorter_name='waveclus_snippets', recording=recording, 
           docker_image='mojack/waveclus',
        #    installation_mode='pypi',
           verbose=True)
# %%
sorting_KS2_5 = run_sorter(sorter_name="kilosort2_5", recording=recording,
                           docker_image=True)
# %%
sorting_IC = run_sorter(sorter_name="ironclust", recording=recording,
                        installation_mode='pypi', docker_image=True)
# %%
