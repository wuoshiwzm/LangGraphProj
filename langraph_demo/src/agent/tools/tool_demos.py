from langchain_core.tools import tool
from pydantic import BaseModel, Field


class CalculateArgs(BaseModel):
    a: float = Field(description='第一个要输入的数字')
    b: float = Field(description='第二个要输入的数字')
    operation: str = Field(description='运算类型，只能是 add, subtract, multiply 和 divide 中的任意一个')


@tool('calculate', args_schema=CalculateArgs, return_direct=False)
def calc(a: float, b: float, operation: str) -> float:
    """工具函数，计算两个数字的运算结果"""
    print(f'call calc func, first num :{a}, second num :{b}, 运算类型:{operation}')
    res = 0.0
    match operation:
        case 'add':
            res = a + b
        case 'subtract':
            res = a - b
        case 'multiply':
            res = a * b
        case 'divide':
            if b != 0:
                res = a / b
            else:
                raise ValueError('divide by zero')
    return res
