---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["AI ML", "Security", "Platform Engineering", "Kubernetes Core", "Community Governance"]
speakers: ["Shuting Zhao", "Nirmata", "Dahu Kuang", "Alibaba Cloud"]
sched_url: https://kccnceu2026.sched.com/event/2CW72/evolving-policy-management-with-agentic-ai-kyverno-mcp-and-kagent-for-multi-cluster-governance-shuting-zhao-nirmata-dahu-kuang-alibaba-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Evolving+Policy+Management+with+Agentic+AI%3A+Kyverno+MCP+and+Kagent+for+Multi-Cluster+Governance+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Evolving Policy Management with Agentic AI: Kyverno MCP and Kagent for Multi-Cluster Governance - Shuting Zhao, Nirmata & Dahu Kuang, Alibaba Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Security]], [[Platform Engineering]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Shuting Zhao, Nirmata, Dahu Kuang, Alibaba Cloud
- Schedule: https://kccnceu2026.sched.com/event/2CW72/evolving-policy-management-with-agentic-ai-kyverno-mcp-and-kagent-for-multi-cluster-governance-shuting-zhao-nirmata-dahu-kuang-alibaba-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Evolving+Policy+Management+with+Agentic+AI%3A+Kyverno+MCP+and+Kagent+for+Multi-Cluster+Governance+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Evolving Policy Management with Agentic AI: Kyverno MCP and Kagent for Multi-Cluster Governance.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW72/evolving-policy-management-with-agentic-ai-kyverno-mcp-and-kagent-for-multi-cluster-governance-shuting-zhao-nirmata-dahu-kuang-alibaba-cloud
- YouTube search: https://www.youtube.com/results?search_query=Evolving+Policy+Management+with+Agentic+AI%3A+Kyverno+MCP+and+Kagent+for+Multi-Cluster+Governance+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kd7R-LhPLak
- YouTube title: Evolving Policy Management with Agentic AI: Kyverno MCP and Kagent for... Shuting Zhao & Dahu Kuang
- Match score: 0.914
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/evolving-policy-management-with-agentic-ai-kyverno-mcp-and-kagent-for/kd7R-LhPLak.txt
- Transcript chars: 21117
- Keywords: cluster, policy, remote, security, clusters, policies, report, status, working, deploy, kivero, skills, including, violations, install, manage, across, kimono

### Resumo baseado na transcript

I didn't expect this many people to attend in the last day all afternoon of the conference but welcome. Um you might have seen that our session originally titled this kivero mp mcp server and k agent but as we're you know built out this solution and the demo for this stage the project evolved into something much more fun and uh we've moved are all my production cluster ready you have to jump between different screens and type a lot of commands uh including cubecuddle uh just to figure out you know to access the logs the events and all the uh reporting system to see hey whether uh your cluster is you know security compliance or not and this is a lot of boring right and a lot of manual work of course we we want to be more efficient automated than that. And finally this is not a daily challenge but uh we as a maintainer are facing it every day. You just carry that okay your cluster is functioning everything is working and then imagine something like just install the pot security standard policy to my cluster and give me the report without doing the you know hem deploy of the kerno policies chart without

### Excerpt da transcript

Uh welcome everyone. Um welcome to the session. I didn't expect this many people to attend in the last day all afternoon of the conference but welcome. Um you might have seen that our session originally titled this kivero mp mcp server and k agent but as we're you know built out this solution and the demo for this stage the project evolved into something much more fun and uh we've moved beyond just connecting clusters to actually orchestrating with them uh with intelligence and that evolution is open cloud and if you came here to learn how to manage manage policies across hundreds of clusters without losing your m mind you're in exactly the right place. All right, so before we dive into the details for today, a quick introduction of our speakers. I'm shooting uh a caverno co-author and maintainer uh working at Namada which is the company behind Civero as a staff engineer. Hi everyone, I'm Dahu Kuang from Alibaba cloud and I'm focus on the continuous security and we are also the fans and the users of Kono community and we have also met a lots of requirements from our user.

>> Thank you. Um all right uh before we dive into the solution dive into the how I wanted to spend a few minutes to talk about the challenges uh that we as platform engineer facing every day right so imagine like in your daily work uh as an platform engineer we no longer deal with the uh just one cluster right we're dealing with many clusters with different versions different uh across different zones with different rules but our two mixes It's difficult and right now if I ask you you know are all my production cluster ready you have to jump between different screens and type a lot of commands uh including cubecuddle uh just to figure out you know to access the logs the events and all the uh reporting system to see hey whether uh your cluster is you know security compliance or not and this is a lot of boring right and a lot of manual work of course we we want to be more efficient automated than that. And what if you have a like assistant uh while you're holding your morning coffee and ask a simple question like you know uh just give me like the production review on my clusters and you can then have a report return it back to you and then you can focusing on those clusters that need some uh to be taken care of.

And the next challenge uh is what I called verification gap. This is the silent killer of security, right? Um I remember there was the other day at kernoccon on this Monday earlie
