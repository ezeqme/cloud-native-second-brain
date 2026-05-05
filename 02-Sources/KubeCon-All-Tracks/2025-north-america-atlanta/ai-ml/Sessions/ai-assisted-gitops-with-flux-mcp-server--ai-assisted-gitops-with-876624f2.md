---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "GitOps Delivery"]
speakers: ["Stefan Prodan", "ControlPlane"]
sched_url: https://kccncna2025.sched.com/event/27Fco/ai-assisted-gitops-with-flux-mcp-server-stefan-prodan-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=AI-Assisted+GitOps+With+Flux+MCP+Server+CNCF+KubeCon+2025
slides: []
status: parsed
---

# AI-Assisted GitOps With Flux MCP Server - Stefan Prodan, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[GitOps Delivery]]
- País/cidade: United States / Atlanta
- Speakers: Stefan Prodan, ControlPlane
- Schedule: https://kccncna2025.sched.com/event/27Fco/ai-assisted-gitops-with-flux-mcp-server-stefan-prodan-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=AI-Assisted+GitOps+With+Flux+MCP+Server+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre AI-Assisted GitOps With Flux MCP Server.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fco/ai-assisted-gitops-with-flux-mcp-server-stefan-prodan-controlplane
- YouTube search: https://www.youtube.com/results?search_query=AI-Assisted+GitOps+With+Flux+MCP+Server+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QAatvo2o-No
- YouTube title: AI-Assisted GitOps With Flux MCP Server - Stefan Prodan, ControlPlane
- Match score: 0.823
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/ai-assisted-gitops-with-flux-mcp-server/QAatvo2o-No.txt
- Transcript chars: 24298
- Keywords: flux, cluster, server, everything, githubs, course, github, actually, little, production, another, llm, clusters, install, latest, request, running, configuration

### Resumo baseado na transcript

So yeah, this talk is about how to to vibe your way into infrastructure. I'm not going to uh actually tell you to do that, but we'll we'll see how it goes. These are some of them, but there are many many challenges of doing GitHubs correctly, right? So part part of this challenge I'm trying to address with what we've built in in Flux NCP, I am going to talk a little bit about that. Um, another big challenge for most organizations is this trade-off between should I go with a monor repo and everybody should, you know, collaborate on a on a single repo, all the apps in there, all your infrastructure and so on or should I, you know, go with a repo per app, a repo per team, right? But let's focus first on you know how we how we solve the the YAML problem.

### Excerpt da transcript

Hello everyone. Uh, thank you very much for making it on the last day of CubeCon. Are you still alive? Y, still going? Yeah. Um, very happy to be here today. Uh, I'm Stfan Pradan. I'm a Flux maintainer for almost eight years now. And in the last eight years, I've been doing a lot of GitHubs. And I'm looking forward now to vibe GitHubs. You know, that's the future. We vibe everything. So yeah, this talk is about how to to vibe your way into infrastructure. No, I'm I'm kidding. I'm not going to uh actually tell you to do that, but we'll we'll see how it goes. Um first, a little bit of introduction. What's Flux? What it does? I'm guessing everybody here uh is aware of what Gittops is. So, Flux is a tool that you deploy on every cluster and it synchronizes your whole uh cluster estate with a desired state which sits outside of the cluster. And here in the first version of Flux, which was many years ago, we we were synchronizing each cluster to a single repo. And of course the desired state is split between what's in the repo and your actual container images.

Um in the latest u form of githubs we call it gitless githubs. Um we basically decided to use the container registry as a unified storage for everything that makes part of your desired state. That means of course the containers, the flux configurations, the Helm charts, maybe you sign and attest everything. So yes, this this is something that you know the flux project has been uh advocating for almost three years now and we we have the beginning of the year we have um made the OCI artifact support in Flux G. So if you are looking at this to migrate your production systems, now is the right time. Uh all the APIs are stable and we have documentation and tooling to allow you to do this migration easily. So yeah, you've adopted GitHubs. Now there are a bunch of challenges. These are some of them, but there are many many challenges of doing GitHubs correctly, right? And I'm going to pick the one in the middle. There is no way out. You are going to be a YAML engineer. You kind of waited. Like seriously, I I'm trying very hard.

I created a couple of years ago a tool called Timony. So you can write with Qang and generate all the YAML, but you'll still have to read them, review pull requests. You can't get away. Um, so maybe we can vibe code YAML in the future, right? So you don't have to type it. So part part of this challenge I'm trying to address with what we've built in in Flux NCP, I am going to talk a littl
