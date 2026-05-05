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
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Arik Alon", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFz0/project-lightning-talk-safe-by-design-ai-powered-auto-healing-for-sres-arik-alon-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Safe+By+Design%3A+AI-Powered+Auto-Healing+For+SREs+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Safe By Design: AI-Powered Auto-Healing For SREs - Arik Alon, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Arik Alon, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFz0/project-lightning-talk-safe-by-design-ai-powered-auto-healing-for-sres-arik-alon-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Safe+By+Design%3A+AI-Powered+Auto-Healing+For+SREs+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Safe By Design: AI-Powered Auto-Healing For SREs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFz0/project-lightning-talk-safe-by-design-ai-powered-auto-healing-for-sres-arik-alon-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Safe+By+Design%3A+AI-Powered+Auto-Healing+For+SREs+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LW8Z8jOGfZE
- YouTube title: Project Lightning Talk: Safe By Design: AI-Powered Auto-Healing For SREs - Arik Alon, Maintainer
- Match score: 0.95
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-safe-by-design-ai-powered-auto-healing-for-sres/LW8Z8jOGfZE.txt
- Transcript chars: 3866
- Keywords: holmes, basically, someone, actually, remediation, metrics, deployment, health, latency, detected, github, robusta, observability, prometheus, incident, within, minutes, saying

### Resumo baseado na transcript

I'm Ari and the CEO of Robusta and one of the maintainers of Holmes GPT. And what it actually means is it's an AI agent which is connected to all your observability data sources. There is a big drop in one of the in the application metrics like the bidding rate dropped 70%. I'm saying check the bidder deployment health, check the logs for error, check the latency metrics, check if there is more than 10% degradation in any of it. So, in this case, it picked up the health check, it done some queries to Prometheus, it detected the metrics degradation, it checked Kubernetes for the pod logs and then went to GitHub, detected what the issue was in the code and even opened a PR to fix it. So, it can go and trigger some GitHub action or it can go and run some Q3 cube CTL commands to restart the pod or to scale it and so on.

### Excerpt da transcript

Hi everyone. So, a bit about me. I'm Ari and the CEO of Robusta and one of the maintainers of Holmes GPT. So, Holmes GPT is basically an open-source AI SRE. And what it actually means is it's an AI agent which is connected to all your observability data sources. So, anything basically that can be used when troubleshooting. So, it connects to your cloud provider, to your observability data, to Prometheus, to Loki, to Datadog, New Relic, whatever you're using in-house. And then whenever there's an incident or someone is trying to investigate something, instead of an engineer going and digging through the data, you just ask the agent why do I have this pod crashing or this latency issue? And then the agent is going and querying the data and then within a few minutes you get a real root cause analysis of why the issue is happening and how to fix it. And Holmes can also do remediation, which is what this talk is about. Holmes is being used by a lot of companies. We submitted it to the CNCF together with the Microsoft which is using it for the Azure CLI.

Uh So, everything basically or a lot of issues start with someone want to uh merge a PR. So, I've got this PR recently one of the teams wanted to merge a big change. Um probably most of it was done by Cloud Coder or some other coding agent. I reviewed the code, looked decent, I went ahead and merged it. And then something went wrong. There is a big drop in one of the in the application metrics like the bidding rate dropped 70%. Now, in the old world, it could have take very long until someone noticed it. Um but luckily for us, we have Holmes which monitors our environment. And then within a few minutes I got a notification on Slack saying an incident detected by Holmes. And Holmes is telling me there was a deployment of deployment of version 241 and there is some critical issue. There is a drop in the metrics of 70%. There is an a drop in the cache hit ratio and then in the latency there is a big increase. Holmes is showing me some visualization of the data. And it even went and dig deeper into the code base.

It basically tells me someone basically set the TTL cache to zero which basically disabled the cache. And Holmes even done more than that. It went on and opened the PR with actually a fix. And now all I have to do is go and review the PR and merge it and I'm basically done. Um so, this is great. So, how how this actually happened? So, basically we defined a Holmes health check which is basically telling H
