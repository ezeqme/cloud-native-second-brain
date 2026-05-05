---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Marly Salazar", "Integral Ad Science", "Yugo Kobayashi", "SB Intuitions", "Eddie Zaneski", "Maciej Szulik", "Defense Unicorns", "Arda Guclu", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2EF5P/whats-new-with-kubectl-and-kustomize-and-how-you-can-help-marly-salazar-integral-ad-science-yugo-kobayashi-sb-intuitions-eddie-zaneski-maciej-szulik-defense-unicorns-arda-guclu-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=What%27s+New+With+Kubectl+and+Kustomize+%E2%80%A6+and+How+You+Can+Help%21+CNCF+KubeCon+2026
slides: []
status: parsed
---

# What's New With Kubectl and Kustomize … and How You Can Help! - Marly Salazar, Integral Ad Science; Yugo Kobayashi, SB Intuitions; Eddie Zaneski & Maciej Szulik, Defense Unicorns; Arda Guclu, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Marly Salazar, Integral Ad Science, Yugo Kobayashi, SB Intuitions, Eddie Zaneski, Maciej Szulik, Defense Unicorns, Arda Guclu, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2EF5P/whats-new-with-kubectl-and-kustomize-and-how-you-can-help-marly-salazar-integral-ad-science-yugo-kobayashi-sb-intuitions-eddie-zaneski-maciej-szulik-defense-unicorns-arda-guclu-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=What%27s+New+With+Kubectl+and+Kustomize+%E2%80%A6+and+How+You+Can+Help%21+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre What's New With Kubectl and Kustomize … and How You Can Help!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5P/whats-new-with-kubectl-and-kustomize-and-how-you-can-help-marly-salazar-integral-ad-science-yugo-kobayashi-sb-intuitions-eddie-zaneski-maciej-szulik-defense-unicorns-arda-guclu-red-hat
- YouTube search: https://www.youtube.com/results?search_query=What%27s+New+With+Kubectl+and+Kustomize+%E2%80%A6+and+How+You+Can+Help%21+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mfcdIa0NtCo
- YouTube title: What's New With Kubectl and Kustomize … and How You... Marly S, Yugo K, Eddie Z, Maciej S & Arda G
- Match score: 0.802
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/whats-new-with-kubectl-and-kustomize-and-how-you-can-help/mfcdIa0NtCo.txt
- Transcript chars: 22838
- Keywords: delete, control, customize, default, command, around, resource, behavior, actually, cuddle, support, anyone, please, interactive, currently, resources, function, customization

### Resumo baseado na transcript

Thank you all for joining us uh for what's new with cube control and customize and how you can help or like I like to say cub ectal which is the official pronunciation. Marley Salazar from Integral Ad Science, Yugo Kobayashi from SV Institutions, Artaguchu from Red Hat, and Mache Shoulick from Defense Unicorns. Uh k uh anyone try that one cool um if you look at it it's not that bad and it actually resolves a ton of problem. Uh but uh at the core it solves ton of problems that we've been experiencing over the past 10 years uh around YAML limitations. Feel free to test it and uh give us a feedback in case there is any issues and problems. you build a Kubernetes and then you need to build a CLI tool to work with the the Kubernetes.

### Excerpt da transcript

Hello. Thank you all for joining us uh for what's new with cube control and customize and how you can help or like I like to say cub ectal which is the official pronunciation. Uh my name is Eddie Zaneski. I'm joined by a slew of awesome people. Marley Salazar from Integral Ad Science, Yugo Kobayashi from SV Institutions, Artaguchu from Red Hat, and Mache Shoulick from Defense Unicorns. Uh, anyone familiar with what SIG CLI is? Oh, that's great. I love explaining this. So, SIGs are the special interest groups of the Kubernetes project that own different parts of the Kubernetes codebase and project itself. And so, SIGs generally have most of the power in terms of direction and steering for their part of the project. And our SIG owns the CLI tooling. So, customize cube control, uh, a bunch of other libraries and SDKs that you may or not may not be using through a bunch of the tools you use. Uh, but we meet every Wednesday at 9:00 a.m. Pacific time, whether we're doing a bug scrub or we're doing a general SIG meeting where we have an agenda and kind of talk through backlogs and issues.

>> 6 p.m. >> 6 pm uh in Europe, Central Europe time. Uh, so please come join us. Uh we're super friendly and uh yeah, it's a great place to get involved contributing back to this Kubernetes project. So I'm going to hand it off to Yugo to talk through customize. Uh hello, I'm maintainer of customize. Uh customiz what is it? Customize tool that's allow you to customize resource files. Uh latest version of customize is B581. Uh what's happened after last QCon anyway? Uh we introduced propagation name set cor inherit function in 580 but that's contained a regression bug related name set proagation for child names uh child customization y. Uh this issue happen because the implementation is uh propagated to the name space set in the parent name space to all child customization. Uh for example it pes applied from a different file in a child name child customization an empconer uh that is fixed in B 581. Please see detail uh issue number 6044 and please use a new customization. I please use new customiz customiz the binary and uh propagation names current to her function uh that customization stop that function is stopped to name hops to overrite.

Uh since some user rel on our previous behavior, we prompt to add an option to the previous behavior. Uh please see detail for issue number 6058. Uh for example, Helm chameace is not set for all resource is problem. >> Okay. Um if you've eve
