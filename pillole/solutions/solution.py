def num_modi_ric(n_i, n_h):
    assert n_i >= 0 and n_h >= 0
    if n_i == 0:
        return 1
    if n_h == 0:
        return num_modi_ric(n_i-1, 1)
    return num_modi_ric(n_i-1, n_h+1) + num_modi_ric(n_i, n_h-1)

def num_modi(n):
    return num_modi_ric(n, 0)


def elenca_modi_ric(n_i, n_h, pescato_intera, pescato_mezza, history):
    assert n_i >= 0 and n_h >= 0
    if n_i + n_h == 0:
        for move in history:
            move()
    elif n_i == 0:
        elenca_modi_ric(0, n_h-1, pescato_intera, pescato_mezza, history + [pescato_mezza]);
    elif n_h == 0:
        elenca_modi_ric(n_i-1, 1, pescato_intera, pescato_mezza, history + [pescato_intera]);
    else:
        elenca_modi_ric(n_i-1, n_h+1, pescato_intera, pescato_mezza, history + [pescato_intera])
        elenca_modi_ric(n_i, n_h-1, pescato_intera, pescato_mezza, history + [pescato_mezza])

# for debubbing in isolation:        
#def pescato_intera():
#    print("I")
#
#def pescato_mezza():
#    print("M")
        
def elenca_modi(n, pescato_intera, pescato_mezza):
    elenca_modi_ric(n, 0, pescato_intera, pescato_mezza, [])

