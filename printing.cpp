// return GB/s
float toBW(int bytes, float sec) {
    return static_cast<float>(bytes) / (1024. * 1024. * 1024.) / sec;
}

float toGFLOPS(int ops, float sec) {
    return static_cast<float>(ops) / 1e9 / sec;
}
