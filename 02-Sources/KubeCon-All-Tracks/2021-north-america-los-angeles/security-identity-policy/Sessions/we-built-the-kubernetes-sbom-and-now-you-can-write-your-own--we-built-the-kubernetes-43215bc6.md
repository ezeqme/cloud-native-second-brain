---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Adolfo García Veytia", "uServers"]
sched_url: https://kccncna2021.sched.com/event/lV64/we-built-the-kubernetes-sbom-and-now-you-can-write-your-own-adolfo-garcia-veytia-uservers
youtube_search_url: https://www.youtube.com/results?search_query=We+Built+the+Kubernetes+SBOM+and+Now+You+Can+Write+Your+Own%21+CNCF+KubeCon+2021
slides: []
status: parsed
---

# We Built the Kubernetes SBOM and Now You Can Write Your Own! - Adolfo García Veytia, uServers

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Adolfo García Veytia, uServers
- Schedule: https://kccncna2021.sched.com/event/lV64/we-built-the-kubernetes-sbom-and-now-you-can-write-your-own-adolfo-garcia-veytia-uservers
- Busca YouTube: https://www.youtube.com/results?search_query=We+Built+the+Kubernetes+SBOM+and+Now+You+Can+Write+Your+Own%21+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre We Built the Kubernetes SBOM and Now You Can Write Your Own!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV64/we-built-the-kubernetes-sbom-and-now-you-can-write-your-own-adolfo-garcia-veytia-uservers
- YouTube search: https://www.youtube.com/results?search_query=We+Built+the+Kubernetes+SBOM+and+Now+You+Can+Write+Your+Own%21+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=N0ZNdnnHL40
- YouTube title: We Built the Kubernetes SBOM and Now You Can Write Your Own! - Adolfo García Veytia, uServers
- Match score: 0.877
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/we-built-the-kubernetes-sbom-and-now-you-can-write-your-own/N0ZNdnnHL40.txt
- Transcript chars: 24719
- Keywords: release, images, container, little, source, artifacts, package, actually, inside, actual, document, output, produce, binaries, dependencies, information, directory, wanted

### Resumo baseado na transcript

so hi and welcome everyone uh thanks for attending the session i know it's uh fridays and the conferences are always the best the worst uh days to have a session in the morning um my name is alofa garcia and i am one of the tech leads with kubernetes release and so just a little bit about me i worked for my whole life for my own company and then they until they pandemic hit and had to switch jobs and i i am now a senior devops engineer tooling to facilitate the production of automated releases if you take a look at this statement miss mission statement it doesn't specifically say kubernetes in it that is why we try to produce some of our tools uh as and may make them as general

### Excerpt da transcript

so hi and welcome everyone uh thanks for attending the session i know it's uh fridays and the conferences are always the best the worst uh days to have a session in the morning um my name is alofa garcia and i am one of the tech leads with kubernetes release and so just a little bit about me i worked for my whole life for my own company and then they until they pandemic hit and had to switch jobs and i i am now a senior devops engineer at marmost um i have two little girls and i also like to travel the world with my bicycle whenever i can and so the beginning of this year i let the effort to produce an s bond for kubernetes um all right so let's start a little bit to talk a little bit about sig release and what we do so sig release is a special interest group that does the kubernetes releases whenever you see a new kubernetes patch release or a new version coming out uh we are the guys that work to make that happen uh so we also form the kubernetes release team um that is managed by the kubernetes release lead who's joining us today here hi ray and we also manage the actual decision of what goes uh what goes what gets cherry picked to the supported branches of kubernetes and uh the the other thing we do that is maybe worth considering today is that we are in task of continually improving the kubernetes release process to keep it up to date to practice the same best best practices and standards that you keep coming up so i wanted to talk a little bit uh before we go into the husband thing about what is in a kubernetes release i wanted to go briefly into this because the kubernetes release has many different kinds of artifacts many different ways of distribution and so we think it's a good example of why having an s bomb is a beneficial thing for a project of this size so the most people are used to how consuming kubernetes by its container images we produce five different images for five different architectures and if you cross that together you get 25 images but there's a lot more to a kubernetes release than just the images we those images are produced we support three different operating systems linux macos windows we have we built some of the artifacts and the images for uh the what we call the supported platforms uh which are currently the 386 amd armor 64.

the bpc60 and that's the idms 390x platform we as i said before we have 25 images with each release we produce 53 naked binaries the naked banners are what you whenever you download for example a c
