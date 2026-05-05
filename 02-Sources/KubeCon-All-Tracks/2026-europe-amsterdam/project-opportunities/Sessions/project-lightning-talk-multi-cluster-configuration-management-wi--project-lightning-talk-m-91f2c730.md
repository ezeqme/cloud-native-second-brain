---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Andy Anderson", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFxk/project-lightning-talk-multi-cluster-configuration-management-with-kubestellar-andy-anderson-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Multi-Cluster+Configuration+Management+With+KubeStellar+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Multi-Cluster Configuration Management With KubeStellar - Andy Anderson, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Andy Anderson, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFxk/project-lightning-talk-multi-cluster-configuration-management-with-kubestellar-andy-anderson-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Multi-Cluster+Configuration+Management+With+KubeStellar+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Multi-Cluster Configuration Management With KubeStellar.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFxk/project-lightning-talk-multi-cluster-configuration-management-with-kubestellar-andy-anderson-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Multi-Cluster+Configuration+Management+With+KubeStellar+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OjxgoDvl82w
- YouTube title: Project Lightning Talk: Multi-Cluster Configuration Management With KubeStellar - Andy Anderson
- Match score: 0.998
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-multi-cluster-configuration-management-with-kub/OjxgoDvl82w.txt
- Transcript chars: 6353
- Keywords: clusters, cuddle, access, aggregate, console, coupube, github, missions, number, stellar, workflows, claude, gemini, looking, projects, configuration, management, second

### Resumo baseado na transcript

I'm here to talk to you today about Coupe Stellar, but specifically about Coupe Stellar console. So, we uh we did a lot of work in the past on something we call Cube Stellar Legacy, which just really focused on deployment and orchestration. So you can use natural language to design missions that use our MCP servers which are deploy and ops which will go out and do the some of the most common exercises that you would normally do with coupe cuddle but does it behind the scenes. You can work to design prompts over and over again and maybe get lucky and be able to save them away in an MD file and maybe you'll remember where that MD file is someday. Go to console.cubstellar.io and click on the demo mode and instantly you'll be given a nice little blurb about how to run a curl command that'll install this in 60 seconds or less. So if any of you one of you want to steer this project to help your enterprise solve big problems, I promise you, come see us.

### Excerpt da transcript

Hi everybody. Welcome to Amsterdam. I love it here. This is the second or third time I'm here. Love this town. All right. I'm here to talk to you today about Coupe Stellar, but specifically about Coupe Stellar console. So, we uh we did a lot of work in the past on something we call Cube Stellar Legacy, which just really focused on deployment and orchestration. But this time around, I'm coming to visit you on lessons learned from that and where we've headed next. So, this is all about AI and cloud native, the marriage of it. And this is the world's first fully integrated and automated Kubernetes management and orchestration solution. Yeah, some of you might think it's AI slop. We don't allow human PRs in this repo. So you can all gasp now. Oo, how's that happening? Anyway, this is based on my experience of almost 10 years of working on Kubernetes clusters. I'm tired. My hands have got arthritis. I don't know about any of you. By show of hands, are you tired of running coupe cuddle commands? Yeah, there's a hell of a lot more than you than that.

Come on, admit it. Okay. So, what we designed this console to do, right, is it's multicluster first. All right. So, that means you're going to have all the CL the access to all of your clusters that you have that you have organized in your coupube config. And yes, it ddupes them so you don't get those multiple versions of the same cluster. Okay. This only has access to what you have access to. So, if your coupube config and your configuration and your API only allows you to have readonly access, you only have readonly access. So we're not exposing anything more than what you naturally have exposure to. This is fully AI powered as I mentioned before. No human PRs are allowed. We use GitHub agentic workflows which is fairly new. Has anybody heard of GitHub agentic workflows? A spattering. Okay. Not many of you. Okay. And that uses of course you know GitHub agent underneath the GitHub agent workflows. We use things like Claude and Gemini and Codeex. And also we use co-pilot underneath the covers which is also using claude opus and gemini and codecs.

Okay. So you can use natural language to design missions that use our MCP servers which are deploy and ops which will go out and do the some of the most common exercises that you would normally do with coupe cuddle but does it behind the scenes. Now you're saying to me right now you're probably looking at me going why don't I just use claude CLI? Why don't I just use Gemin
