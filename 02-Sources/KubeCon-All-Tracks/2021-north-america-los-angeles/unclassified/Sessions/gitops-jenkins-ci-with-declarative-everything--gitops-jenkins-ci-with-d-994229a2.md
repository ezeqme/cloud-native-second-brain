---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Unclassified"
themes: ["GitOps Delivery"]
speakers: ["Kingdon Barrett", "Weaveworks"]
sched_url: https://kccncna2021.sched.com/event/lV0V/gitops+jenkins-ci-with-declarative-everything-kingdon-barrett-weaveworks
youtube_search_url: https://www.youtube.com/results?search_query=GitOps%2BJenkins-CI+With+Declarative+Everything+CNCF+KubeCon+2021
slides: []
status: parsed
---

# GitOps+Jenkins-CI With Declarative Everything - Kingdon Barrett, Weaveworks

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Los Angeles
- Speakers: Kingdon Barrett, Weaveworks
- Schedule: https://kccncna2021.sched.com/event/lV0V/gitops+jenkins-ci-with-declarative-everything-kingdon-barrett-weaveworks
- Busca YouTube: https://www.youtube.com/results?search_query=GitOps%2BJenkins-CI+With+Declarative+Everything+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre GitOps+Jenkins-CI With Declarative Everything.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0V/gitops+jenkins-ci-with-declarative-everything-kingdon-barrett-weaveworks
- YouTube search: https://www.youtube.com/results?search_query=GitOps%2BJenkins-CI+With+Declarative+Everything+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rtkBnADRpNE
- YouTube title: GitOps+Jenkins-CI With Declarative Everything - Kingdon Barrett, Weaveworks
- Match score: 0.849
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/gitops-jenkins-ci-with-declarative-everything/rtkBnADRpNE.txt
- Transcript chars: 25005
- Keywords: jenkins, flux, actually, cluster, repository, probably, update, little, automation, defined, already, release, policy, declarative, artifacts, version, commit, latest

### Resumo baseado na transcript

awesome thanks everyone for coming um i'm kingdom this is my first time at kubecon in person uh really glad to be here uh so welcome everyone to the jenkins and git ops talk this is my first talk at kubecon obviously well in person i've presented a couple of times before i'm kingdom as i said as taylor introduced me i'm an open source support engineer at weaveworks i'm also a flux maintainer and i'm the cow on twitter if you want to follow me that would be cool

### Excerpt da transcript

awesome thanks everyone for coming um i'm kingdom this is my first time at kubecon in person uh really glad to be here uh so welcome everyone to the jenkins and git ops talk this is my first talk at kubecon obviously well in person i've presented a couple of times before i'm kingdom as i said as taylor introduced me i'm an open source support engineer at weaveworks i'm also a flux maintainer and i'm the cow on twitter if you want to follow me that would be cool um so gitops that's what you're all here for i think first uh we're going to talk really briefly about what is get ops get ops is an operational model for cloud native operations it's a modern model i think i meant to say so get ops is formally defined at this point this should give you an idea of its maturity we've gone through lots of rounds in a vendor-neutral setting aws i believe red hat microsoft a number of companies have participated weave works code fresh to come up with this definition for get ops and we think it's pretty solid at this point so it's been made 1.0.0 um that's that's awesome so the get ops definition is a set of principles um and i want to preface this by saying that this is not prescriptive or requirements of git ops git ops is uh a progressive progress you have to process you have to [Music] take one step before you can uh get all the way there so step one is understanding uh declarative artifacts you have you already have declarative artifacts if you're like kubecon great step one out of the way step two is they should be in a versioned store which is uh holds immutable artifacts so version store um in this case could be git could be something else uh this is the vendor-neutral definition so try to be as inclusive as possible and another guideline of of the gitops principles is that they should be automatically pulled from your source oops and it's a continuous reconciling process so so continuous delivery continuous reconciling you have reconcilers that sit inside of the cluster they pull artifacts and they apply them to the cluster from a version store in a continuous process and the artifacts are declarative the git repository should completely describe the state of your system so that it can be reproduced so okay back to this talk and why you're here um i i have an idea of who my intended audience is but i don't know every one of you so i'm not sure if you're all current jenkins users can we get a show of hands lots of current jenkins users okay great you're you're my
