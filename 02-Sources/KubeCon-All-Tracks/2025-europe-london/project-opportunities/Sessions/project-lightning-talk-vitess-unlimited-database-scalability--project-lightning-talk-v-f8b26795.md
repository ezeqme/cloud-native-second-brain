---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Storage Data", "SRE Reliability", "Community Governance"]
speakers: ["Shlomi Noach", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcwU/project-lightning-talk-vitess-unlimited-database-scalability-shlomi-noach-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Vitess%3A+Unlimited+Database+Scalability+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Vitess: Unlimited Database Scalability - Shlomi Noach, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Shlomi Noach, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcwU/project-lightning-talk-vitess-unlimited-database-scalability-shlomi-noach-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Vitess%3A+Unlimited+Database+Scalability+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Vitess: Unlimited Database Scalability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcwU/project-lightning-talk-vitess-unlimited-database-scalability-shlomi-noach-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Vitess%3A+Unlimited+Database+Scalability+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ERztKTd-ckA
- YouTube title: Project Lightning Talk: Vitess: Unlimited Database Scalability - Shlomi Noach, Maintainer
- Match score: 0.913
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-vitess-unlimited-database-scalability/ERztKTd-ckA.txt
- Transcript chars: 3951
- Keywords: sharding, database, probably, google, shards, unlimited, relational, approach, scheme, vitess, scaling, source, framework, stored, served, github, running, created

### Resumo baseado na transcript

Um I'm standing in um replacing Dipy Zigeredi, the uh leader of the project who unfortunately could not come here today and I'm here to talk to you about uh unlimited scaling in Vit. So Vit is an open source CNCF project graduated about six or seven years ago. So the most obvious thing you can do is to scale out right your uh data is growing. and really tune fine-tune it to match your application's uh query patterns. You can scale out with more shards, uh, commodity hardware, or you can scale up your servers, use less shards, then scale out.

### Excerpt da transcript

Hi everyone, thank you for coming. My name is Schlomi. I'm with Planet Scale and a Vites maintainer for the past five years. Um I'm standing in um replacing Dipy Zigeredi, the uh leader of the project who unfortunately could not come here today and I'm here to talk to you about uh unlimited scaling in Vit. What's unlimited scaling anyway? So Vit is an open source CNCF project graduated about six or seven years ago. It's a sharded distributed uh relational database framework that runs on top of my scale. You've probably used it. You are probably using it. Every message you send in Slack is stored and served by Vitess. Every pull request on GitHub is stored and served by Vites. Cashup blocks Cash App uses Vit. And these companies are able to serve many millions of queries per second out of a relation database uh using vit. So there's a large community and a large user base. We actually don't really know what we don't know. Uh it's open source so you never know who's using your product, right? Uh I think in this room many can uh can relate.

you know, a user pops in in Slack, asks some question, turns out there there's this mass operation they're running, you know, critical app in some different country we've never heard of before. Where did you come from? Who are you? So, um, we keep we keep hearing about new users, um, large users and keep getting more input from the community. So the V test story is uh a bit peculiar. It was created by YouTube to store and serve their entire video metadata and uh YouTube was sub subsequently purchased by Google and as part of that Google migrated VES into probably one of the most hostile environments a relational database can expect to run on which was uh Google's Borg. Borg is the predecessor to Kubernetes. And so Vitz is kind of one probably the first relational database to run at scale on a Kubernetes like environment and uh Google uh later on moved on to uh run its own infrastructure and uh contributed vitf and we've been maintaining it ever since. Vitz achieves scale by sharding. You may have heard about uh auto sharding.

That's not how Vest works. It takes a different approach. It takes a an approach of custom or configurable sharding key. It's a key design choice for VES. It comes at a cost upfront. You as a user need to think about your sharding scheme, need to think about your data and how you might want to approach your data. That's the cost. But once you buy into the sharding world on you're in sharding sphere
