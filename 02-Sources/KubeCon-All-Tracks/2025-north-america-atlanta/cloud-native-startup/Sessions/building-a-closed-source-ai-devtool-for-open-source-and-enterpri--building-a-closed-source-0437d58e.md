---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Cloud Native Startup"
themes: ["AI ML", "Community Governance"]
speakers: ["Devin Stein", "Dosu"]
sched_url: https://kccncna2025.sched.com/event/2AY1S/building-a-closed-source-ai-devtool-for-open-source-and-enterprise-devin-stein-dosu
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+Closed-Source+AI+DevTool+for+Open+Source+and+Enterprise+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Building a Closed-Source AI DevTool for Open Source and Enterprise - Devin Stein, Dosu

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Cloud Native Startup]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Devin Stein, Dosu
- Schedule: https://kccncna2025.sched.com/event/2AY1S/building-a-closed-source-ai-devtool-for-open-source-and-enterprise-devin-stein-dosu
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+Closed-Source+AI+DevTool+for+Open+Source+and+Enterprise+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Building a Closed-Source AI DevTool for Open Source and Enterprise.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/2AY1S/building-a-closed-source-ai-devtool-for-open-source-and-enterprise-devin-stein-dosu
- YouTube search: https://www.youtube.com/results?search_query=Building+a+Closed-Source+AI+DevTool+for+Open+Source+and+Enterprise+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NWt6aXn6pDE
- YouTube title: Building a Closed-Source AI DevTool for Open Source and Enterprise - Devin Stein, Dosu
- Match score: 0.966
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/building-a-closed-source-ai-devtool-for-open-source-and-enterprise/NWt6aXn6pDE.txt
- Transcript chars: 23711
- Keywords: source, maintainers, documentation, product, knowledge, enterprises, maintainer, actually, github, information, issues, question, developers, within, closed, basically, strategy, growth

### Resumo baseado na transcript

Um, and also open source maintainer for softs, customized softs, and spark magic, which I'll be talking a bit about today. Uh, and so today, uh, we're going to be talking about the case for building, uh, closed source AI dev tools for open source maintainers and enterprises. So it helped us focus on uh the common problems between open source maintainers and enterprises and not get too um pushed in either direction. Uh, at the time, you know, the AI tooling was fairly new and, uh, it was very slow getting started in enterprises, uh, because of concerns around security. There's not a lot of people coming to open source maintainers and saying like, "Hey, can we solve your problems?" Um and you know if you are able to solve these problems uh they're a very outspoken minority. Um and like the kind of three lessons that we've learned is one is like you know really around focus on the problem between open source uh and enterprises.

### Excerpt da transcript

Let's get started. Um, one, thank you all for being here. Really appreciate you showing up. Um, I'm Devin Stein for those of you who don't know me. Uh, founder and CEO of DOSU. Um, and also open source maintainer for softs, customized softs, and spark magic, which I'll be talking a bit about today. Uh, and so today, uh, we're going to be talking about the case for building, uh, closed source AI dev tools for open source maintainers and enterprises. So this talk was partially inspired by this tweet slash interaction on Twitter. Um for those of you who maybe didn't see this, this is the maintainer of Zod, a popular um open source library, you know, jokingly tweeting basically, can someone make a product for open source maintainers to help them save time on issue triage um and documentation? Um and then you know quickly shortly after his reaction when he found out that a product like this actually does exist and we've built it. Um and the reason you know one he didn't think anyone would build this and then two was so surprised when there was a product for him uh was you know open source maintainers aren't exactly you know a huge market for startups to go after.

Um it's a relatively tiny population of developers. um they have very low willingness to pay. Uh and then you know as a maintainer myself I can say that they're you know very um opinionated uh group of developers as well. not the easiest people to please. Um but uh you know we chose to you know uh work with and sell to open source maintainers and enterprises and it's been really effective strategy for us and um I think it both helps u open source maintainers and enterprises and I want to get into kind of the details of like how we ended up doing this um and what's worked for us um and we'll go from there. Just to set some context about DOSU for those of you who also don't know, do is an AI native knowledge tool for engineering teams. And so what this means is we make it really really easy to generate um documentation sort of as a byproduct of building as developers build um or from wherever they work. Uh we make it extremely easy to maintain knowledge and documentation to actually keep it in sync as code changes.

do will review changes uh for your code with respect to your knowledge base. Uh and then importantly, we actually help you make use of your knowledge. So we share it wherever it's needed um whether that's Slack or Microsoft Teams or in the case of uh open source in GitHub issues and discussi
