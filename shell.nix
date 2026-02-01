{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell
{
	nativeBuildInputs = with pkgs; [
	  thonny # to interface with raspberry pi pico
		python312Packages.python # python 
	  python312Packages.matplotlib	# matplotlib
	  python312Packages.pandas      # to analyse data
	  python312Packages.jupyterlab  # interactive notebooks
	];
}
