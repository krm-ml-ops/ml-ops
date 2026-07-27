{
  description = "Required development shell for the Fundamentals of MLOps course";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/0c2094806c9e542f31785ef3569ab9e900e3ce9c";

  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
    in {
      devShells = forAllSystems (system:
        let pkgs = import nixpkgs { inherit system; };
        in {
          default = pkgs.mkShell {
            packages = [
              pkgs.python311
              pkgs.uv
              pkgs.git
              pkgs.nodejs_22
            ];
          };
        });
    };
}
