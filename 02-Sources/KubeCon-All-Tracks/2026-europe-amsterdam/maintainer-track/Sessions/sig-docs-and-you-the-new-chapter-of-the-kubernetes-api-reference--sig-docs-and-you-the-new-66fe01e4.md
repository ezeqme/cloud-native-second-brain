---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Kat Cosgrove", "Minimus", "Lavish Pal", "Independent", "Rey Lejano", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2EF6Q/sig-docs-and-you-the-new-chapter-of-the-kubernetes-api-reference-generator-kat-cosgrove-minimus-lavish-pal-independent-rey-lejano-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Docs+and+You%3A+The+New+Chapter+of+the+Kubernetes+API+Reference+Generator+CNCF+KubeCon+2026
slides: []
status: parsed
---

# SIG Docs and You: The New Chapter of the Kubernetes API Reference Generator - Kat Cosgrove, Minimus; Lavish Pal, Independent; Rey Lejano, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Kat Cosgrove, Minimus, Lavish Pal, Independent, Rey Lejano, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2EF6Q/sig-docs-and-you-the-new-chapter-of-the-kubernetes-api-reference-generator-kat-cosgrove-minimus-lavish-pal-independent-rey-lejano-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Docs+and+You%3A+The+New+Chapter+of+the+Kubernetes+API+Reference+Generator+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre SIG Docs and You: The New Chapter of the Kubernetes API Reference Generator.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6Q/sig-docs-and-you-the-new-chapter-of-the-kubernetes-api-reference-generator-kat-cosgrove-minimus-lavish-pal-independent-rey-lejano-red-hat
- YouTube search: https://www.youtube.com/results?search_query=SIG+Docs+and+You%3A+The+New+Chapter+of+the+Kubernetes+API+Reference+Generator+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xnHsQE7bg7o
- YouTube title: SIG Docs and You: The New Chapter of the Kubernetes API Ref... Kat Cosgrove, Lavish Pal & Rey Lejano
- Match score: 0.834
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/sig-docs-and-you-the-new-chapter-of-the-kubernetes-api-reference-gener/xnHsQE7bg7o.txt
- Transcript chars: 19215
- Keywords: reference, generator, release, actually, generate, python, process, documentation, looking, handling, simple, schema, possible, co-chair, generating, someone, cubernetes, already

### Resumo baseado na transcript

So you are a bit tired but bear with us and believe me this is going to be really quick one. So here we are and s dogs and you the new chapter of Kubernetes API reference generator. So, so building on that as we already already shared that there will be some problem in running the Kubernetes API reference generator and like it fails regularly without any error message and all. And so now after this pull request you will get the clear message like what went wrong and the another area uh where things were bit confusing that how the tool look uh locates the kubernetes repo because the build expected it to be in a fixed path like kx.io/cubernetes io/ kubernetes and which is I don't know how most people actually clone it and so even with a correct step the build can also fail. So instead of trying to guess different paths the approach was simplified by requiring a k root variable and my intention was to add that you don't need to follow that step that you have to rename the k uh kubernetes repo to k.io/cubernetes io/cubernetes

### Excerpt da transcript

Hello everyone. Thank you for being here. I know this is one of the last talk and on the last day. So you are a bit tired but bear with us and believe me this is going to be really quick one. So here we are and s dogs and you the new chapter of Kubernetes API reference generator. Before starting here's a quick intro about mine. Hi everyone, I'm Lavish Pal. I'm Alfx mentee at Kubernetes and ATC contributor. Hello everybody. My name is Cat Cosg Gro. I am a tech lead for SIG Docs. I'm also on the Kubernetes steering committee and I'm the release team sub project owner. Hello, my name is Ray Lano. I am a co-chair of SIGDOCS, a tech lead as well. I'm also a SIG security sub project lead as well. So, this talk is about the API reference generator. So if you've ever used our documentation um you know that we have a reference guide to all the APIs to uh to the cube API server to cube control and metric server and other components as well. Uh so generating these docs is during uh before write every release is usually very difficult.

Uh so someone from the release team so for if you don't know Kubernetes releases three times a year and one of my favorite uh hobbies is to look at the docs on the new alpha features and the graduating features as well. Uh part of the uh new docs is the API reference docs and someone from the release team uh generates the tries to generate the the reference docs. Uh and you can see here there's a number of dependencies there's GCC uh python go very specific versions as well uh pyaml uh and a lot more and the example here is the some of the commands uh to generate the the reference stocks for the cubernetes API so as you could see it is uh quite complex especially for someone who has not used it before. So that's uh most time if you don't know the release team uh does have uh a lot of new folks into into the project. So this might be the very first time that they're looking at these steps and looking at these dependencies. So we often get lots of failures. This example for me uh back in five years ago where I tried to generate uh some of the reference docs and it failed and this happens quite frequently for about the past four years or so.

And we also get a lot and we hear about it. Um so there's examples from Slack that hey the API reference docs for this for the latest versions is not updated. We also get GitHub issues on it as well and we know about this. I know a month before each release I know that this is going to come. So we he
