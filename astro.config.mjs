import { defineConfig } from "astro/config";

const repoName = process.env.GITHUB_REPOSITORY?.split("/")[1] ?? "duawowns";

export default defineConfig({
  site: "https://duawowns.github.io",
  base: `/${repoName}/`,
});