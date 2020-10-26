# OOD

## SOLID 原则
### Single responsibility principle
一个类只做一件事情
- Calculate area 一个类
- Print area 一个类
### Open close principle
对象或实体对拓展开放，对修改封闭
- 设计一个抽象类
- 调用的时候输入应该是抽象类，具体函数实现在具体类

### Liskov substitution priciple 
任何一个子类或者派生类应该可以替换父类

### Interface segregation principle
不应该强迫一个类实现他用不上的接口

### Dependency inversion principle
抽象不应该依赖于具体实现，具体实现应该依赖于抽象
high-level实体不应该依赖于low-level实体

## 5c
### Clarify
- what:
    - 取关键字，提问是什么样的，什么样的elevator，有什么属性
    - Do we need to consider xxx?

### Clsss object
我们不需要知道actor，actor只是用来帮助理解work flow，我们在设计的时候，不需要加入那些actor。
例如设计停车场，我们不需要汽车class，因为对我们设计没有帮助，parking slot可能有不同分类，但是我们不需要car object。