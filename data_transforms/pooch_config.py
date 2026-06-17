import pooch

fido = pooch.create(
	path=pooch.os_cache("rte-examples"),
	base_url="https://aux.ecmwf.int/ecpds/home/ckdmip/concentrations/",
)
fido.load_registry("./rte-examples-registry.txt",)

def list_files(pattern):
	return [fido.fetch(n) for n in fido.registry.keys() if pattern in n]
