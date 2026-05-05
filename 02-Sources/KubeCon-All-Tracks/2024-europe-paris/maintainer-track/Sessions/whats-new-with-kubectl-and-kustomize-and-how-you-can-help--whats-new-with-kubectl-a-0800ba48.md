---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Eddie Zaneski", "Defense Unicorns", "Maciej Szulik", "Red Hat"]
sched_url: https://kccnceu2024.sched.com/event/1YhjU/whats-new-with-kubectl-and-kustomize-and-how-you-can-help-eddie-zaneski-defense-unicorns-maciej-szulik-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=What%27s+New+with+Kubectl+and+Kustomize+%E2%80%A6+and+How+You+Can+Help%21+CNCF+KubeCon+2024
slides: []
status: parsed
---

# What's New with Kubectl and Kustomize … and How You Can Help! - Eddie Zaneski, Defense Unicorns & Maciej Szulik, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Eddie Zaneski, Defense Unicorns, Maciej Szulik, Red Hat
- Schedule: https://kccnceu2024.sched.com/event/1YhjU/whats-new-with-kubectl-and-kustomize-and-how-you-can-help-eddie-zaneski-defense-unicorns-maciej-szulik-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=What%27s+New+with+Kubectl+and+Kustomize+%E2%80%A6+and+How+You+Can+Help%21+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre What's New with Kubectl and Kustomize … and How You Can Help!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhjU/whats-new-with-kubectl-and-kustomize-and-how-you-can-help-eddie-zaneski-defense-unicorns-maciej-szulik-red-hat
- YouTube search: https://www.youtube.com/results?search_query=What%27s+New+with+Kubectl+and+Kustomize+%E2%80%A6+and+How+You+Can+Help%21+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LjXZjt_yOJ8
- YouTube title: What's New with Kubectl and Kustomize … and How You Can Help! - Eddie Zaneski & Maciej Szulik
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/whats-new-with-kubectl-and-kustomize-and-how-you-can-help/LjXZjt_yOJ8.txt
- Transcript chars: 32123
- Keywords: control, actually, command, client, commands, changes, delete, resource, little, version, server, remember, information, currently, around, resources, convert, default

### Resumo baseado na transcript

hey everyone thank you very much for showing up I know we're we're at the last session of today so Hal uh heart well uh heartfelt thank you for for actually showing up this late yeah everyone stoked to learn about uh Cube control huh yeah that's awesome so uh I'm Eddie zeneski I'm joined by ma shulik uh we are the tech leads for 6 CLI there's a few others of us on the 6 CLI leadership team um and yeah yeah 6 CLI is the special interest group on both additional changes that were somewhat notable were already at that point in time we had plugable scheduler uh although it did require you to recompile the entire kubernetes to include your plugins and some basic admission uh plugins that you might be familiar with today uh post 1.0 we've seen a bunch of uh changes some of these might be familiar maybe you worked with kubernetes when these were introduced um support for get extensions plugin CLI runtime uh that was a big change in uh qctl where we talk through an agenda talk through stuff and then we alternate every of the off weeks for a cube control bug scrub or a customized bug scrub so those are great for you to come in kind of learn how we we look at

### Excerpt da transcript

hey everyone thank you very much for showing up I know we're we're at the last session of today so Hal uh heart well uh heartfelt thank you for for actually showing up this late yeah everyone stoked to learn about uh Cube control huh yeah that's awesome so uh I'm Eddie zeneski I'm joined by ma shulik uh we are the tech leads for 6 CLI there's a few others of us on the 6 CLI leadership team um and yeah yeah 6 CLI is the special interest group for the CLI tooling of the kubernetes project uh kubernetes is divided up into different special interest groups and each one is responsible for a different part of the project so we own the CLI tooling uh we had a release 129 go out a few months ago you may have seen it um couple things we shipped we had sub plugins that landed in Cube control uh for create so you can actually create sub commands that have your own create uh specification so you can do like Cube control create my thingy and you can build a plugin for that we also had some stuff that shipped with help and weight uh 130 is uh we're currently in I think beta zero is what's cut yep yep yep we are in the 130 release process right now so you should see it in the next couple of weeks uh we have some pretty cool features that are landing in Alpha we have a uh custom profiles for cube control to bug these are you can specify different resource profiles and set comp profiles that you want for your debug containers it's a long ass feature so get in there play with it give it a try when you when you get 130 dropped uh another big project that's been worked on is transitioning from Speedy to websockets uh Speedy is the kind of what http2 called before http2 was a real thing so it's super old super deprecated uh it's used everywhere for all of our streaming and Long Live Connections inside of kubernetes uh there's a big effort that's been going on shout out to Sean Sullivan for cutting that over to use websockets for a modern approach uh you will see that land in beta which is awesome and two big stable features that landed Cube control delete now has interactive delete which is Super Rad I'll show you that in a second uh and we finally moving aggregated Discovery to stable which means that your Discovery time should like go down yeah like significantly down I I'll talk about it in a minute when we be going through major features that we went through but awesome uh Cube control delete Das uh take a look at this slide how many times does this happen to you where you
