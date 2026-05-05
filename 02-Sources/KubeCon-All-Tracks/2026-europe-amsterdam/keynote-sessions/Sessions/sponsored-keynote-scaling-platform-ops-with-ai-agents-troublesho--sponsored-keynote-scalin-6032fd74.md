---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Keynote Sessions"
themes: ["AI ML", "Platform Engineering", "SRE Reliability"]
speakers: ["Jorge Palma", "Principal PDM Manager", "Microsoft", "Natan Yellin", "CEO", "Robusta"]
sched_url: https://kccnceu2026.sched.com/event/2HgFq/sponsored-keynote-scaling-platform-ops-with-ai-agents-troubleshooting-to-remediation-jorge-palma-principal-pdm-manager-microsoft-natan-yellin-ceo-robusta
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Scaling+Platform+Ops+with+AI+Agents%3A+Troubleshooting+to+Remediation+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Sponsored Keynote: Scaling Platform Ops with AI Agents: Troubleshooting to Remediation - Jorge Palma, Principal PDM Manager, Microsoft & Natan Yellin, CEO, Robusta

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jorge Palma, Principal PDM Manager, Microsoft, Natan Yellin, CEO, Robusta
- Schedule: https://kccnceu2026.sched.com/event/2HgFq/sponsored-keynote-scaling-platform-ops-with-ai-agents-troubleshooting-to-remediation-jorge-palma-principal-pdm-manager-microsoft-natan-yellin-ceo-robusta
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Scaling+Platform+Ops+with+AI+Agents%3A+Troubleshooting+to+Remediation+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: Scaling Platform Ops with AI Agents: Troubleshooting to Remediation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2HgFq/sponsored-keynote-scaling-platform-ops-with-ai-agents-troubleshooting-to-remediation-jorge-palma-principal-pdm-manager-microsoft-natan-yellin-ceo-robusta
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Scaling+Platform+Ops+with+AI+Agents%3A+Troubleshooting+to+Remediation+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Apha61UYfLY
- YouTube title: Sponsored Keynote: Scaling Platform Ops with AI Agents: Troubleshootin... Jorge Palma & Natan Yellin
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/sponsored-keynote-scaling-platform-ops-with-ai-agents-troubleshooting/Apha61UYfLY.txt
- Transcript chars: 5318
- Keywords: actually, customers, production, operator, agents, headlamp, flux, gadget, environment, problems, connect, troubleshooting, probably, become, day-to-day, windows, typical, on-call

### Resumo baseado na transcript

So, we've all seen how AI's becoming pervasive and we've all been told that we probably should be using it to become more productive. But, that can become a bit cumbersome when we're find ourselves between our day-to-day tools, different chat windows, asking them questions, copy-pasting from our tools to different context windows, then going back and doing something with those tools again. It catches the problems in production as soon as they're rolled out and something goes wrong and before your customers know this. With operator mode, you can ship at the speed of AI and also catch problems and fix them at the speed of AI.

### Excerpt da transcript

So, we've all seen how AI's becoming pervasive and we've all been told that we probably should be using it to become more productive. But, that can become a bit cumbersome when we're find ourselves between our day-to-day tools, different chat windows, asking them questions, copy-pasting from our tools to different context windows, then going back and doing something with those tools again. Wouldn't it be great if that were actually well, fluid and integrated? George, you work with a ton of Acast customers. How do they do that on a day-to-day basis? Well, we have a lot of different customers with different tool sets, but there's a few tools that stand out that are very, very common. One of them is Headlamp, the Kubernetes UI that is part of the SIG UI as a subproject, and it's an extensible and simple UI that allows you to manage clusters and applications. We also see them use things like Home GPT, which is an agent for operations as well as SREs. And we've seen them as we've seen today on stage that they're using GitOps flows with things like Flux.

So, let's see how we can put all together and troubleshoot an issue that one of our users is having. So, we're Contoso, we're a pet store, and one of our users is making a purchase for things like catnip and some cat toys. And so, they're going to add to their cart, and they're going to try and check out, typical flow, but there's an issue. So, they're going to open a ticket and it's going to go to one of our on-call engineers who luckily has no idea what's going on and is going to go into Headlamp and ask the AI assistant, which is powered by Home GPT, to about what's going on. And he's hoping it's not the NS once again cuz it's been apparently typical. So, here Home GPT's actually going to leverage a myriad of tools such as Cube CTL, of course, but also things like the Inspector Gadget tool set. So, it's going to run a EBPF gadget from Inspector Gadget to do a TCP dump, figure out that it's actually calling a order. -service that doesn't exist. What exists is orders, plural, -service, and it actually found that as well when listing the services.

So, it's telling me, "Hey, there's a typo here. You're pointing to the wrong service that doesn't exist." And it analyzed that looking at the TCP dump and where the application was calling. So, now I'm telling it, "All right, go right ahead. Please submit the PR. Give me a good description cuz I need to hotfix this, so I need to give this to my incident management."
