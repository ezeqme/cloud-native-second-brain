---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Application + Delivery"
themes: ["AI ML", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Katrina Verey", "Shopify"]
sched_url: https://kccnceu2023.sched.com/event/1Hycs/1m-lines-of-yaml-wrangling-kubernetes-configuration-for-hundreds-of-teams-katrina-verey-shopify
youtube_search_url: https://www.youtube.com/results?search_query=1M+Lines+of+YAML%3A+Wrangling+Kubernetes+Configuration+for+Hundreds+of+Teams+CNCF+KubeCon+2023
slides: []
status: parsed
---

# 1M Lines of YAML: Wrangling Kubernetes Configuration for Hundreds of Teams - Katrina Verey, Shopify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Application + Delivery]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Katrina Verey, Shopify
- Schedule: https://kccnceu2023.sched.com/event/1Hycs/1m-lines-of-yaml-wrangling-kubernetes-configuration-for-hundreds-of-teams-katrina-verey-shopify
- Busca YouTube: https://www.youtube.com/results?search_query=1M+Lines+of+YAML%3A+Wrangling+Kubernetes+Configuration+for+Hundreds+of+Teams+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre 1M Lines of YAML: Wrangling Kubernetes Configuration for Hundreds of Teams.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hycs/1m-lines-of-yaml-wrangling-kubernetes-configuration-for-hundreds-of-teams-katrina-verey-shopify
- YouTube search: https://www.youtube.com/results?search_query=1M+Lines+of+YAML%3A+Wrangling+Kubernetes+Configuration+for+Hundreds+of+Teams+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rFtKguVs5jw
- YouTube title: 1M Lines of YAML: Wrangling Kubernetes Configuration for Hundreds of Teams - Katrina Verey, Shopify
- Match score: 0.949
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/1m-lines-of-yaml-wrangling-kubernetes-configuration-for-hundreds-of-te/rFtKguVs5jw.txt
- Transcript chars: 30718
- Keywords: config, artifact, review, resources, framework, changes, actually, release, configuration, developers, wanted, making, needed, commit, templating, resource, platform, revision

### Resumo baseado na transcript

hello and welcome to this talk one million lines of yaml wrangling kubernetes configuration for hundreds of teams my name is Katrina very and I work for Shopify specifically I'm a senior staff software and engineer who works in infrastructure engineering at Shopify and I've been using kubernetes since Shopify first started experimenting with it back in 2016.

### Excerpt da transcript

hello and welcome to this talk one million lines of yaml wrangling kubernetes configuration for hundreds of teams my name is Katrina very and I work for Shopify specifically I'm a senior staff software and engineer who works in infrastructure engineering at Shopify and I've been using kubernetes since Shopify first started experimenting with it back in 2016. more recently I've had the honor to co-lead 6 CLI and cust it's customize and care and function sub-projects the reason you might be interested in my opinion on config management besides that I work in that area with six CLI is that I worked on shopify's production platform teams since its early days and I was responsible for both the doing and the redoing of a bunch of the decisions that we made related to config management this talk is going to be a story about how Shopify has managed an enormous amount of kubernetes yaml first in a way that didn't work super well and then in a way that worked much better both for our platform team and for the developers that we serve but the story itself isn't really the main point all orgs at the scale are different and I'm not going to try to tell you to do exactly what we did at the end I will introduce an open source toolkit that you can use to take a similar approach if you would like to but I'm not going to go through the vast array of tooling options out there there are a lot of talks that already do that my main hope is that you'll leave this talk understanding why some configuration Management Systems will work out better than others and cause you less pain still going to be config management it's not going to be no pain but I also hope that you'll take away some principles for designing your own systems before we dive in though I want to share with you why I think this problem is more interesting than it might sound and hopefully convince you that it's not just a big headache that you just have to deal with yes managing large volumes of data in a white space sensitive language is a pain but let's take a moment to appreciate what we're really doing here we're not talking about managing arbitrary yaml documents we're talking about managing your documents that contain kubernetes objects and those objects are really really important because kubernetes is API Centric the declarative data that we're talking about is really at its core this data in our yaml files is the means through which we express the state that we want our systems to have so that the various
