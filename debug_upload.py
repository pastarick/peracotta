from extract_data import extract_and_collect_data_from_generated_files
from upload import upload_to_tarallo

data = extract_and_collect_data_from_generated_files(directory='tmp',
                                                                 has_dedicated_gpu=False,
                                                                 gpu_in_cpu=True,
                                                                 verbose=False)
upload_to_tarallo(data)
