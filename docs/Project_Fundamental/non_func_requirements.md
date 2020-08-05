# 基于软件质量模型的非功能需求与场景

![](https://github.com/Invincible-Inc/Final-Work/blob/master/docs/Project_Fundamental/non_func_requirements_image/1.png)

### 1.功能适用性
 - 定义：当软件在指定条件下使用时，软件产品提供满足明确和隐含需要的功能的能力。
 - 功能完整性(functional completeness)：是否覆盖所有主要case；需求明确提出的case覆盖比例；隐含case覆盖量。
 - 功能正确性(functional correctness)：所有case(明确与隐含)的正确比例。
 - 功能方便性(functional appropriateness)：用户通过该软件完成其目标的方便程度，所有case的完成步骤的简化程度。
 
### 2.性能效率
 - 定义：在规定条件下，相对于所用资源的数量，软件产品可提供适当性能的能力。
 - 时间特性(time behaviour): 时间相关的性能。
 - 资源占用率(resource utilization)：rom, ram, cpu, gpu, port等资源的占用程度。
 - 容量(capacity): 软件能力在空间上的边界。
 
### 3.xxxxxxx
 
 - xxxx：xxxxxx
 - xxxx：xxxxxx
 - xxxx：xxxxxx
 
### 5.可靠性 
 
 - 定义：产品在规定的时间内，在规定的条件下，完成预定功能的能力，它包括结构的安全性，适用性和耐久性。
 - 成熟度：定义、评价软件开发过程的成熟度，并提供提高软件质量的指导。
 - 可用性：可用性是在某个考察时间，系统能够正常运行的概率或时间占有率期望值。它是衡量设备在投入使用后实际使用的效能，是设备或系统的可靠性、可维护性和维护支持性的综合特性。
 - 容错性：使系统在部分组件（一个或多个）发生故障时仍能正常运作的能力。
 - 可恢复性：将你的部署恢复到故障发生时状态的能力。迅速从系统故障或灾难中恢复的能力不仅取决于是否有数据的当前备份，还在于是否存在预先制定的在新的硬件上恢复该数据的计划。

### 6.安全性 
 
 - 定义：使软件在受到恶意攻击的情形下依然能够继续正确运行及确保软件被在授权范围内合法使用
 - 保密性：指网络信息不被泄露给非授权的用户、实体或过程。
 - 完整性：用户、进程或者硬件组件具有能力，能够验证所发送或传送的东西的准确性，并且进程或硬件组件不会被以任何方式改变。
 - 不可抵赖性：对自己行为的不可抵赖及对行为发生的时间的不可抵赖。
 - 审查追踪：对所有的访问信息建模，并记录日志，供日后的分析，抓住可疑分子，采取相应的措施，如黑名单，收回授权等等。
 - 真实性：反映事物真实情况的程度。
 
### 7.可维护性
* 定义：软件产品可被修改的能力。修改可能包括修正、改进或软件对环境、需求和功能规格说明变化的适应
* 模块化：软件由各个组件组成，改变一个组件对其他组件的影响程度。比如要求模块划分清晰，松耦合高内聚等。
* 易分析性（降低定位缺陷的成本）：软件产品诊断软件中的缺陷或失效原因或识别待修改部分的能力。比如log、cache内容导出、调试shell帮助快速定位，以及从用户收集数据等。
* 易改变性（降低修改缺陷的成本）：软件产品使指定的修改可以被实现的能力。设计上封装性好、高内聚（同层设计时，一个实体只完成一个功能）低耦合、为未来可能的变化留有扩充余地。
* 稳定性：软件产品避免由于软件修改而造成意外结果的能力。
* 易测试性（降低发现缺陷的成本）：软件产品使已修改软件能被确认的能力。即软件发现故障并隔离、定位其故障的能力特性。
* 维护性的依从性：软件产品遵循与维护相关的标准或约定的能力。

### 8.可移植性
* 定义：软件产品从一种环境迁移到另外一种环境的能力。
* 适应性：软件产品无需采用有别于为考虑该软件的目的而准备的活动或手段就可能适应不同的指定环境的能力(兼容性)。
* 易安装性：软件产品在指定环境中被安装的能力。比如安装类型有文本界面、图像向导式、绿色软件等。
* 共存性：软件产品在公共环境中同与其分享公共资源的其它独立软件共存的能力。
* 易替换性：软件产品在同样环境下，替代另一个相同用途的指定软件产品的能力。即升级能力、打补丁能力等。
* 可移植性的依从性：软件产品遵循与可移植性相关的标准或约定的能力。