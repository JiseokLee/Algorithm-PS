vk, jk = map(int, input().split())
va, ja = map(int, input().split())
vh, dh, jh = map(int, input().split())

heavyChain = vh * dh * jh
lightChainK = vk * jk
lightChainA = va * ja

print(heavyChain * (lightChainK + lightChainA))