def combine_cuts(cuts_dict=dict(), cut_name=None):
    CUTS = str()
    for CUT in cuts_dict[cut_name]:
        if CUT == cuts_dict[cut_name][-1]:
            CUTS += CUT
            break
        CUTS += CUT + ' & '
    return CUTS
