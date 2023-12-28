# MODULO

## I. Bài toán tìm UCLN dựa trên thuật toán Euclid

```
Số chia: a
Số bị chia: b
Tìm UCLN của a và b: d = UCLN(a,b) = ?
```
```
Gán r0 = a
    r1 = b
```
Ta có phép chia: <b>$r_0$ = $r_1$*$q_1$ + $r_2$</b>

$r_0$ = $r_1$ * $q_1$ + $r_2$<br>
$r_1$ = $r_2$ * $q_2$ + $r_3$<br>
$r_2$ = $r_3$ * $q_3$ + $r_4$<br>
...... ...... ...... ......<br>
$r_{m-1}$ = $r_m$ * $q_m$ + $r_{m+1}$<br>
$r_m$ = $r_{m+1}$ * $q_{m+1}$ + $r_{m+2}$<br>

Thuật toán dừng lại khi <b>$r_{m+2}$ = 0</b>

Lúc này USCLN cần tìm là: <b>d = UCLN($r_0$, $r_1$) = $r_{m+1}$</b> 

> Chính là số dư của phép chia được thực hiện ngay trước phép chia cuối cùng cho số dư = 0


```python
def UCLN(a, b):
    r0, r1 = a, b
    q1, r2 = r0 // r1, r0 % r1
    while r2 != 0:
        r0, r1 = r1, r2
        q1, r2 = r0 // r1, r0 % r1
    return r1
```

## II. Thuật toán Euclid mở rộng

Thuật toán Euclid cho rằng:<br>
Nếu d = UCLN(a, b), thì tồn tại 2 số nguyên x, y thỏa mãn:

```a*x + b*y = d```

Bài toán đặt ra là tìm 2 số x, y<br>
Để làm điều này ta tìm x, y theo hệ thức truy hồi.<br>
Nghĩa là sẽ tìm xi, yi sao cho:

```a*xi + b*yi = ri (với i=0,1,2,3...)```

```
Với x0 = 1, y0 = 0
    => a*1 + b*0 = r0
    => r0 = a```

Với x1 = 0, y1 = 1
    => a*0 + b*1 = r1
    => r1 = b
```
Tổng quan:

$$
a * x_i + b * y_i = r_i\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad (1)
$$

$$
=> a * x_{i+1} + b * y_{i+1} = r_{i+1} \qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad \ \ (2)
$$

Lại có:<br>

$$
r_i = r_{i+1} * q_{i+1} + r_{i+2} \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad
$$

$$
=> r_i - r_{i+1} * q_{i+1} = r_{i+2} \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\ \ \ \ \ (3)
$$   

Thay (1),(2) vào (3) ta được:

$$ 
(a \cdot x_i + b \cdot y_i) - (a  \cdot  x_{i+1} + b  \cdot  y_{i+1})  \cdot  q_{i+1} = r_{i+2} \qquad\qquad\qquad\qquad \
$$

$$
=> a \cdot  (x_i - x_{i+1} \cdot q_{i+1}) + b  \cdot (y_i - y_{i+1} \cdot q_{i+1}) = r_{i+2} \qquad\qquad\qquad \ (4)
$$

Lại có: 

$$
a \cdot x_{i+2} + b \cdot y_{i+2} = r_{i+2}\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad \ \ (5)
$$ 

Từ (4), (5) ta được:

$$
\begin{cases}
x_{i+2} = x_i - x_{i+1} \cdot q_{i+1} \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\\
y_{i+2} = y_i - y_{i+1} \cdot q_{i+1}
\end{cases}
$$

```python
def Euclid_Extended(a, b):
    r0, r1 = a, b
    q1, r2 = r0//r1, r0%r1
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    x2, y2 = x0 - x1*q1, y0 - y1*q1
    while r2 != 0:
        x0, x1 = x1, x2
        y0, y1 = y1, y2
        r0, r1 = r1, r2
        q1, r2 = r0//r1, r0%r1
        x2, y2 = x0 - x1*q1, y0 - y1*q1
    return r1, x1, y1

res = Euclid_Extended(29,8)
print(res)
#res = (1, -3, 11)
        
```
Với a = 29, b = 8
<table border="1">
<tbody>
    <tr>
        <td>Step</td>
        <td>r_i</td>
        <td>r_i+1</td>
        <td>r_i+2</td>
        <td>q_i+1</td>
        <td>x_i</td>
        <td>x_i+1</td>
        <td>x_i+2</td>
        <td>y_i</td>
        <td>y_i+1</td>
        <td>y_i+2</td>
</tr>
<tr>
<td>0</td>
<td>29</td>
<td>8</td>
<td>5</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>-3
</td></tr>
<tr>
<td>1</td>
<td>8</td>
<td>5</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>-1</td>
<td>1</td>
<td>-3</td>
<td>4
</td></tr>
<tr>
<td>2</td>
<td>5</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>-1</td>
<td>2</td>
<td>-3</td>
<td>4</td>
<td>-7
</td></tr>
<tr>
<td>3</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>-1</td>
<td>2</td>
<td>-3</td>
<td>4</td>
<td>-7</td>
<td>11
</td></tr>
<tr>
<td>4</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td></tr></tbody></table>

Kết quả:

$$
\begin{cases}
d = UCLN(29,8) = r_1 = 1\\
x = x_1 = -3 \\
y = y_1 = 11 \\
29 * -3 + 8 * 11 = 1
\end{cases}
$$