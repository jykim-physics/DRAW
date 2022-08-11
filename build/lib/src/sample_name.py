def sample_name(option=None, location=None, sample_info=None ):

    for i in sample_info['location']:
        if i == location:
            ccbar_sample = sample_info['location'][location] + sample_info[option]['ccbar']
            charged_sample = sample_info['location'][location] + sample_info[option]['charged']
            mixed_sample = sample_info['location'][location] + sample_info[option]['mixed']
            uubar_sample = sample_info['location'][location] + sample_info[option]['uubar']
            ddbar_sample = sample_info['location'][location] + sample_info[option]['ddbar']
            ssbar_sample = sample_info['location'][location] + sample_info[option]['ssbar']
            taupair_sample = sample_info['location'][location] + sample_info[option]['taupair']

            sample_location={}
            sample_location["ccbar"]=ccbar_sample
            sample_location["charged"]=charged_sample
            sample_location["mixed"]=mixed_sample
            sample_location["uubar"]=uubar_sample
            sample_location["ddbar"]=ddbar_sample
            sample_location["ssbar"]=ssbar_sample
            sample_location["taupair"]=taupair_sample

    return sample_location
