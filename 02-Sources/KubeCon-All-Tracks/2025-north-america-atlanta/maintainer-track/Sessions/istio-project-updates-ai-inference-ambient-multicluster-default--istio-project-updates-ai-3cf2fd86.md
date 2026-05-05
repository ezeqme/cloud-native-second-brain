---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Kubernetes Core", "Community Governance"]
speakers: ["Keith Mattix", "Microsoft"]
sched_url: https://kccncna2025.sched.com/event/27NoI/istio-project-updates-ai-inference-ambient-multicluster-default-deny-keith-mattix-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Istio+Project+Updates%3A+AI+Inference%2C+Ambient+Multicluster+%26+Default+Deny+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Istio Project Updates: AI Inference, Ambient Multicluster & Default Deny - Keith Mattix, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Keith Mattix, Microsoft
- Schedule: https://kccncna2025.sched.com/event/27NoI/istio-project-updates-ai-inference-ambient-multicluster-default-deny-keith-mattix-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Istio+Project+Updates%3A+AI+Inference%2C+Ambient+Multicluster+%26+Default+Deny+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Istio Project Updates: AI Inference, Ambient Multicluster & Default Deny.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NoI/istio-project-updates-ai-inference-ambient-multicluster-default-deny-keith-mattix-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Istio+Project+Updates%3A+AI+Inference%2C+Ambient+Multicluster+%26+Default+Deny+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vdCMLZ-4vUo
- YouTube title: Istio Project Updates: AI Inference, Ambient Multicluster & Default Deny - Keith Mattix, Microsoft
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/istio-project-updates-ai-inference-ambient-multicluster-default-deny/vdCMLZ-4vUo.txt
- Transcript chars: 31056
- Keywords: gateway, traffic, inference, policy, request, cluster, waypoint, default, network, extension, clusters, ambient, within, policies, multicluster, pretty, called, requests

### Resumo baseado na transcript

I want to first thank you for making the trek all the way over here to to building C. Uh I did not realize how far away this was when I saw it on the schedule, but thanks for being here with me to talk about the SEO project and hear about the latest and greatest that we've been working on. It's been around for a bit, but it's the standard way to describe traffic that's happening within and into a Kubernetes cluster. Like I mentioned, it's a new sub project within Kubernetes and it extends the personabased gateway API model to include roles and personas that are focused on doing uh inference. And so one inference pool equals a set of compute for a model that's running inside a Kubernetes cluster. So, one of the ways of thinking about GIE is that it is a specialized routing architecture for LLM inference.

### Excerpt da transcript

I want to first thank you for making the trek all the way over here to to building C. Uh I did not realize how far away this was when I saw it on the schedule, but thanks for being here with me to talk about the SEO project and hear about the latest and greatest that we've been working on. I'm Keith, I'm a principal engineer at Microsoft and a member of the SEO technical oversight committee. And uh yeah, I'm here on behalf of the rest of the TOC to talk to you about uh this amazing project that we all know and hopefully love. Uh so to nobody's surprise, we're going to talk about AI. Um if you've been at KubeCon for uh this week and you've been reading the news, everybody's talking about it. So I figured we'd do a little bit of uh audience participation here when it comes to everybody's AI use. So um when I, you know, could ask some questions and do a quick survey here. How many of you are serving AI models in Kubernetes today? Either staging or proding AI models. Okay, pretty good number of you. Good number of you.

Okay. Uh, how many of you hope to be running AI models in Kubernetes by this time next year? This time next year, hope to be running models. Another good amount of people. Okay. Next three years. Same group about the same. All right. So, maybe longer time horizon for some of you. Okay. How many of you aren't serving AI models, but you're consuming AI? So from OpenAI, Vert.Ex, AI foundry, bedrock. How many of you raise your hand if you're consuming AI models from third party providers? Okay. Yeah. Most looks like the biggest group we've had so far. All right. Shifting a little bit to Aentic. How many of you are deploying MCP servers in your uh environments today? Raise your hand. Deploying MCP servers. All right. How many are planning to deploy MCP servers, but you're not today? Wow. I think we've got most people in this room fall into some of those categories, but just in case if you haven't raised your hand yet and you don't want to feel left out. How many of you want nothing to do with AI or anything I just said, raise your hand?

Well, hey, well, I I'll take it. Some of you are double raising. It's It's okay. It's fine. But my point with this is to say that no matter where you are in your AI journey today, Isio wants to be a part of that journey. And I think we can be with some of the stuff we've been working on over the past uh couple of releases, we're doing some really cool things to bring is IO into the AI age. So the first thing I want
