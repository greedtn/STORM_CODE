# 各変数のValidation結果まとめ
| 変数 | Validation結果 |
|------|----------------|
| 気圧の係数  | False       |
| Pressure Drop  | True          |
| 気圧と風速の係数  | True          |
| 発生時のΔPt  | True         |
| 発生時の場所  | True          |
| 発生月  | True          |
| MSLP  | True          |
| ポアソン分布の係数  | True          |

→ InputDataは間違ってなさそう <br>
→ 気圧の係数に関しては、コードをいじっているので違っていて当然。コードを戻して検証する必要あり