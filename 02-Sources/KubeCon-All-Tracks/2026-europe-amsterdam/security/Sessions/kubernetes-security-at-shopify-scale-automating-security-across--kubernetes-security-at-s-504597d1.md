---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["Security", "Kubernetes Core", "SRE Reliability"]
speakers: ["Jie Wu", "Pulkit Garg", "Shopify"]
sched_url: https://kccnceu2026.sched.com/event/2CW3b/kubernetes-security-at-shopify-scale-automating-security-across-an-infrastructure-monorepo-jie-wu-pulkit-garg-shopify
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Security+at+Shopify+Scale%3A+Automating+Security+Across+an+Infrastructure+Monorepo+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Kubernetes Security at Shopify Scale: Automating Security Across an Infrastructure Monorepo - Jie Wu & Pulkit Garg, Shopify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jie Wu, Pulkit Garg, Shopify
- Schedule: https://kccnceu2026.sched.com/event/2CW3b/kubernetes-security-at-shopify-scale-automating-security-across-an-infrastructure-monorepo-jie-wu-pulkit-garg-shopify
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Security+at+Shopify+Scale%3A+Automating+Security+Across+an+Infrastructure+Monorepo+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Kubernetes Security at Shopify Scale: Automating Security Across an Infrastructure Monorepo.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW3b/kubernetes-security-at-shopify-scale-automating-security-across-an-infrastructure-monorepo-jie-wu-pulkit-garg-shopify
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Security+at+Shopify+Scale%3A+Automating+Security+Across+an+Infrastructure+Monorepo+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fBEG2kag4Aw
- YouTube title: Kubernetes Security at Shopify Scale: Automating Security Across an Infrastr... Jie Wu & Pulkit Garg
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/kubernetes-security-at-shopify-scale-automating-security-across-an-inf/fBEG2kag4Aw.txt
- Transcript chars: 23024
- Keywords: developers, security, semgrep, infrastructure, secure, production, changes, follow, findings, single, controls, hundreds, better, actually, manifest, mischief, pipeline, container

### Resumo baseado na transcript

Um today we're going to going to to take you all on a journey in how we secure Kubernetes at Shopify. Uh so, what we do is we help secure infrastructure for millions of merchants. So, all those services you just saw, so where is the Kubernetes manifest files that defines them? Every misconfiguration that ever snuck through a code review, a security review, every bad configuration that someone just copy and paste. With all this scale, all the infrastructure, all these merchants, all the problems that we just described, something really had to change. So, we sat down as a team, looked at the problem, and came up with a plan.

### Excerpt da transcript

Everyone, thank you all for joining us. Um we're very excited to be here. Um today we're going to going to to take you all on a journey in how we secure Kubernetes at Shopify. Uh my name is Jay. Um I'm really excited to be here visiting Amsterdam. I flew in from New York City. So, that tells you two things about myself. I really like pizza and I walk very fast. And I'm joined here today with my colleague My name is uh Pulkit. I'm from Ottawa, Canada originally. And I've been in three different time zones in the last 2 weeks. So, still a bit jet lagged, but super pumped to be here. And first time attending, first time speaking. Yeah. So, we're both on the infrastructure security team at Shopify. Uh so, what we do is we help secure infrastructure for millions of merchants. Um and but for today, our official title is professional cat herders. Um so, what is Kubernetes security at scale? It is like herding cats. Well, except that these cats can accidentally expose your entire infrastructure. So, uh let us show you what do we mean.

So, let's set the scene here. Uh welcome to Captain Q's kingdom. You might recognize Captain Q from Fifi and Friends. Um so, you got server land, you have cluster island, you have deploy road, you have uh helm workshop. Um all of this uh at the center is held together by the monorepo. Uh which we'll dive into later on. Um this is a lot to take in already. So, Pulkit, let's walk through the scale. We run hundreds of services on K8s, making it an extremely important part of our infrastructure. Our developers push almost 60K deploys each week, which is just going to increase as we keep scaling up and growing. All of this means we have close to 500 clusters deployed worldwide in different regions and zones. With all this massive infrastructure, we power millions of merchants and help run their online stores. Now, with everything this, let's look at how all of this set up in the back end. So, all those services you just saw, so where is the Kubernetes manifest files that defines them? Where is the helm charts that the developers use them to template?

Where is the deploy configurations that helps them roll them out? What are the policies in place to better govern them? All them live in one place, the infrastructure monorepo. Which give uh which give us one source of truth, but also one source of risk. A single change here can ripple across everything. So, who makes all those changes? And this is where we introduce Dev, which is a uh deve
