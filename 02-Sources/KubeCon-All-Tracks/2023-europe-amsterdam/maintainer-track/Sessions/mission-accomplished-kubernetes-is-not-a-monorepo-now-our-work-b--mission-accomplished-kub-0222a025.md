---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Justin Santa Barbara", "Google", "Ciprian Hacman", "Microsoft"]
sched_url: https://kccnceu2023.sched.com/event/1HycF/mission-accomplished-kubernetes-is-not-a-monorepo-now-our-work-begins-justin-santa-barbara-google-ciprian-hacman-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Mission+Accomplished%3A+Kubernetes+Is+Not+a+Monorepo.+Now+Our+Work+Begins%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Mission Accomplished: Kubernetes Is Not a Monorepo. Now Our Work Begins! - Justin Santa Barbara, Google & Ciprian Hacman, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Justin Santa Barbara, Google, Ciprian Hacman, Microsoft
- Schedule: https://kccnceu2023.sched.com/event/1HycF/mission-accomplished-kubernetes-is-not-a-monorepo-now-our-work-begins-justin-santa-barbara-google-ciprian-hacman-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Mission+Accomplished%3A+Kubernetes+Is+Not+a+Monorepo.+Now+Our+Work+Begins%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Mission Accomplished: Kubernetes Is Not a Monorepo. Now Our Work Begins!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HycF/mission-accomplished-kubernetes-is-not-a-monorepo-now-our-work-begins-justin-santa-barbara-google-ciprian-hacman-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Mission+Accomplished%3A+Kubernetes+Is+Not+a+Monorepo.+Now+Our+Work+Begins%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QbNTNqrsRA0
- YouTube title: Mission Accomplished: Kubernetes Is Not a Monorepo. Now Our Work...- Justin Barbara & Ciprian Hacman
- Match score: 0.887
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/mission-accomplished-kubernetes-is-not-a-monorepo-now-our-work-begins/QbNTNqrsRA0.txt
- Transcript chars: 27323
- Keywords: provider, components, manifest, manifests, testing, production, providers, source, actually, change, single, broken, release, component, publish, number, projects, together

### Resumo baseado na transcript

so our talk today is uh entitled mission accomplished kubernetes is not a mono repo Network begins uh thank you for attending on one of the last slots today uh I am Justin Santa Barbara I have been contributing to kubernetes for I guess longer than I care to admit now I've done a lot of work on the initially on the AWS cloud provider I kicked off the chaops project a number of years ago and I've been at Google Now for a number of years trying to help

### Excerpt da transcript

so our talk today is uh entitled mission accomplished kubernetes is not a mono repo Network begins uh thank you for attending on one of the last slots today uh I am Justin Santa Barbara I have been contributing to kubernetes for I guess longer than I care to admit now I've done a lot of work on the initially on the AWS cloud provider I kicked off the chaops project a number of years ago and I've been at Google Now for a number of years trying to help people with their adoption of kubernetes hi everyone my name is cyprian uh I'm a an Syria ability engineer at Microsoft these days I am also helping companies migrate to kubernetes in and in my spare time I'm a maintainer and contributor to various Cloud native projects okay so this is what we're going to be covering today broadly why did we split up the monorepa why did we go from one big git repository source of Truth into the many repositories that we have today um when we did that did we lose things or was it all just just upside and spoiler uh the things that we did lose how can we get those things back that's what we're gonna be covering today okay uh in the beginning there was one big kubernetes repo so everything in one place uh all components were versioned together like there was no cloud provider or other things uh and there was end-to-end testing um multiple clouds on every PR and that was actually pretty good um it was the right architecture for the time it was actually very easy to make big cross-cutting changes across multiple layers you could have one PR that could change you know the API it could change the cube API server the controller manager Cube cuddle could change the scripts that installed kubernetes you could do that all in one PR and everything would just sort of go together it was a very productive way to move quickly and we had good test coverage as well you know we had test coverage that would test on AWS and gcp we had some other tests on other Cloud providers that um you know were a little bit more complicated but those the AWS and gcp tests were kicked off on every single PR so every time you made any change to kubernetes even if you just changed the docs you know we would make sure that you hadn't broken AWS and you hadn't broken gcp and we were able to test all those all that cloud provider functionality all the functionality in kubernetes on every single PR so it was a good productive place where we were so is it was pretty good but why did we stop doing this uh there were a
