import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "Cloud Native Second Brain",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "pt-BR",
    baseUrl: "ezeqme.github.io/cloud-native-second-brain",
    ignorePatterns: [
      ".github",
      ".git",
      ".obsidian",
      ".quartz",
      "bin",
      "node_modules",
      "public",
      "scripts",
      "_sources",
      "05-Templates",
      "!(*.md)",
    ],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#fbfaf7",
          lightgray: "#e6e2d8",
          gray: "#a8a194",
          darkgray: "#4a4a43",
          dark: "#252620",
          secondary: "#23706b",
          tertiary: "#8b5e34",
          highlight: "rgba(35, 112, 107, 0.14)",
          textHighlight: "#f2da7b88",
        },
        darkMode: {
          light: "#171916",
          lightgray: "#343832",
          gray: "#70796c",
          darkgray: "#d6d7ce",
          dark: "#f1f0e8",
          secondary: "#7cc9bd",
          tertiary: "#d7aa72",
          highlight: "rgba(124, 201, 189, 0.16)",
          textHighlight: "#8f742b88",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
