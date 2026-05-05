---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Unclassified"
themes: ["GitOps Delivery"]
speakers: ["Scott Rigby", "Kingdon Barrett", "Weaveworks"]
sched_url: https://kccnceu2021.sched.com/event/iE1e/helm-users-what-flux-2-can-do-for-you-scott-rigby-kingdon-barrett-weaveworks
youtube_search_url: https://www.youtube.com/results?search_query=Helm+Users%21+What+Flux+2+Can+Do+For+You+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Helm Users! What Flux 2 Can Do For You - Scott Rigby & Kingdon Barrett, Weaveworks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Unclassified]]
- Temas: [[GitOps Delivery]]
- País/cidade: Virtual / Virtual
- Speakers: Scott Rigby, Kingdon Barrett, Weaveworks
- Schedule: https://kccnceu2021.sched.com/event/iE1e/helm-users-what-flux-2-can-do-for-you-scott-rigby-kingdon-barrett-weaveworks
- Busca YouTube: https://www.youtube.com/results?search_query=Helm+Users%21+What+Flux+2+Can+Do+For+You+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Helm Users! What Flux 2 Can Do For You.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE1e/helm-users-what-flux-2-can-do-for-you-scott-rigby-kingdon-barrett-weaveworks
- YouTube search: https://www.youtube.com/results?search_query=Helm+Users%21+What+Flux+2+Can+Do+For+You+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hCTgCRlU-M0
- YouTube title: Helm Users! What Flux 2 Can Do For You - Scott Rigby & Kingdon Barrett, Weaveworks
- Match score: 0.735
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/helm-users-what-flux-2-can-do-for-you/hCTgCRlU-M0.txt
- Transcript chars: 25517
- Keywords: flux, release, controller, customization, install, kingdom, itself, wordpress, caverno, cluster, reconcile, actually, releases, little, installed, version, anything, jenkins

### Resumo baseado na transcript

hi everyone welcome to hell users what can flux 2 do for you with scott radiant king and barrett i'm i'm scott rigby um i'm a helm and flux maintainer working on the developer experience team at wheatworks and i'm kingdom barrett i'm an oss support engineer also working on the developer experience team at weaveworks so yeah first of all welcome uh the assumption for people coming to or watching this recording and coming to the q a are that you have some familiarity with helm there is no

### Excerpt da transcript

hi everyone welcome to hell users what can flux 2 do for you with scott radiant king and barrett i'm i'm scott rigby um i'm a helm and flux maintainer working on the developer experience team at wheatworks and i'm kingdom barrett i'm an oss support engineer also working on the developer experience team at weaveworks so yeah first of all welcome uh the assumption for people coming to or watching this recording and coming to the q a are that you have some familiarity with helm there is no assumption about familiarity with flux yet but we can guess that some people have there's a variety or there's a range of experience so um some some of you may have tried um the current version of fox some of you may have tried the older version of books some may just be looking to get into get ups from your existing from your existing element uh installations and releases so um i think flux's hub controller is the best way to do hell according to get up's principles and our team and and me um in particular i'm dedicated to uh doing whatever i can to help make sure that you feel that way too so please uh in the q a and and outside of that please keep in touch about how you feel about it and what and how it works for you so um so first of all uh i'm just going to explain first for a moment what flux adds on top of what what you already get when you use helm so at least as of film three um i almost designed uh with a client and an sdk on which the client was built um but no running software agents of any kind and this architecture intended anything outside of the client scope to be addressed by other tools in the wider ecosystem which could then make use of helm's sdk just as as the helm client does so why am i even mentioning that it's because uh uh flux's held controller um built on uh kubernetes controller runtime it is uh it's an example of a mature software agent that uses helm's sdk to full effect um every feature at least that is non-experimental is available uh of helm is available in the helm controller using purely using sdk um however there are some things that are added to this otherwise why would you bother using it um the main the main thing that's added is the get out side of things right so so flux's biggest addition is a structured layer for your releases that automatically gets for the release that automatically gets reconciled to your cluster based on the rules that you configure in your in-git or inversion control so the way i like to think about it is hom
