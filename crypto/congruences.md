# Đồng dư thức

Đồng dư mô đun n được ký hiệu là: <b>a ≡ b (mod n)</b>

```
Nếu a đồng dư với b trong modul n

<=> (a - b) mod n = 0
có nghĩa là: (a - b) chia hết cho n
```

## Tính chất 

- ∀c ∈ Z | a≡b [n] ⟹ ac ≡ bc [n]
​
- ∀c ∈ Z | a≡b [n] ⟹ a+c ≡ b+c [n]

- ∀c ∈ Z | a≡b [n] and b≡c [n] ⟹ a≡c [n]

- ∀m ∈ N | a≡b [n] ⟹ a<sup>m</sup> ≡ b<sup>m</sup> [n]

## Chứng minh T/C 1: ∀c ∈ Z | a≡b [n] ⟹ ac ≡ bc [n]

```
Nếu a≡b [n]
⟹ (a-b) mod n = 0
=> c(a-b) mod n = 0 (vì c(a-b) là bội của n)
=> ac ≡ bc [n] (dpcm)
```
## Chứng minh T/C 4: ∀m ∈ N | a≡b [n] ⟹ a<sup>m</sup> ≡ b<sup>m</sup> [n]

>Nếu a≡b [n] ⟹ (a-b) mod n = 0

Xét a<sup>m</sup> - b<sup>n</sup> = (a-b)(a<sup>m-1</sup> + a<sup>m-2</sup>b + a<sup>m-3</sup>b<sup>2</sup> + ... + ab<sup>n-2</sup> + b<sup>n-1</sup> ) <br>
=> a<sup>m</sup> - b<sup>n</sup> là bội của (a-b) <br>
Vậy nếu (a-b) mod n = 0<br>
thì a<sup>m</sup> - b<sup>n</sup> mod n = 0

> Vậy a<sup>m</sup> = b<sup>n</sup> [n]