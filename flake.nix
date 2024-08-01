# RAG using txtai
{
  inputs = {
    dream2nix.url = "github:nix-community/dream2nix";
    nixpkgs.follows = "dream2nix/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
    systems.url = "github:nix-systems/default";
    devenv.url = "github:cachix/devenv";
  };

  outputs = { self, nixpkgs, devenv, systems, dream2nix, ... } @ inputs:
    inputs.flake-utils.lib.eachDefaultSystem (system:
      let

        pkgs = import nixpkgs {
          system = system;
          config.allowUnfree = true;
        };

      in  {
        devShells = 
          let
            python_with_pkgs = (pkgs.python311.withPackages(pp: [ pp.txtai ]));
          in
            {
              default = pkgs.mkShell {
                packages = [
                  pkgs.python311
                ];
                shellHook = ''
                  export PYTHONPATH=${python_with_pkgs}/${python_with_pkgs.sitePackages}:$PYTHONPATH
              '';
              };
            };
      }
    );
}
