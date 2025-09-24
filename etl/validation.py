from pydantic import BaseModel
from pydantic import ConfigDict
import pandas as pd

class DatasetModel(BaseModel):
    data: pd.DataFrame

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def validate_not_empty(cls, df: pd.DataFrame):
        if df.empty:
            raise ValueError("O dataset está vazio!")
        if df.columns.size == 0:
            raise ValueError("O dataset não possui colunas.")
        return df
