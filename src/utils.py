def get_size(W, H, w, h):
    r = w / h
    if r * H > W:
        return (W, int(W / r))
    return (int(H * r), H)