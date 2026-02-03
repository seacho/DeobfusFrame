# DeobfusFrame
deobfus frame


一个轻量级反混淆框架，内置了插件式规则注册与多轮解码能力，便于扩展更多混淆类型。

## 内置支持的混淆类型

- Base64 字符串
- Hex 字符串
- `rev:` 前缀的反转字符串
- `xor:<key>:<hex>` 格式的 XOR 混淆

## 快速开始

```bash
python -m deobfusframe.cli ./samples/input.txt
```

或使用标准输入：

```bash
echo "rev:olleh" | python -m deobfusframe.cli
```

## 扩展新规则

1. 在 `deobfusframe/obfuscations/` 下创建新规则类，继承 `ObfuscationRule`。
2. 实现 `detect` 与 `decode` 方法。
3. 在 `default_registry()` 中注册该规则。

## 设计要点

- **Registry**: 管理规则注册与匹配。
- **Engine**: 支持多轮迭代解码。
- **CLI**: 方便快速验证解码效果。