def auto_repr(obj, class_name: str) -> str:
	p: dict = obj.__dict__
	a = [f"{k}='{v}'" if isinstance(v, str) else f'{k}={repr(v)}' for k, v in p.items()]
	return f'{class_name}({', '.join(a)})'
