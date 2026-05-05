---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Mark Rossetti", "Microsoft", "Jose Valdes", "Red Hat"]
sched_url: https://kccncna2025.sched.com/event/27NoC/kubernetes-sig-windows-updates-mark-rossetti-microsoft-jose-valdes-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+SIG-Windows+Updates+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kubernetes SIG-Windows Updates - Mark Rossetti, Microsoft & Jose Valdes, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Mark Rossetti, Microsoft, Jose Valdes, Red Hat
- Schedule: https://kccncna2025.sched.com/event/27NoC/kubernetes-sig-windows-updates-mark-rossetti-microsoft-jose-valdes-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+SIG-Windows+Updates+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kubernetes SIG-Windows Updates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NoC/kubernetes-sig-windows-updates-mark-rossetti-microsoft-jose-valdes-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+SIG-Windows+Updates+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=au0sO-qDTvw
- YouTube title: Kubernetes SIG-Windows 20230103
- Match score: 0.754
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kubernetes-sig-windows-updates/au0sO-qDTvw.txt
- Transcript chars: 17086
- Keywords: windows, process, release, anybody, images, server, fabian, calico, repository, everybody, anything, containers, probably, update, getting, working, around, everything

### Resumo baseado na transcript

hello everybody and welcome to the January 3rd 2023 iteration of the kubernetes Sig Windows uh community meeting as always these meetings are recorded and uploaded to YouTube so be sure to adhere to the cncf code of conduct um we're just coming off of some U.S holidays here so kind of might be a little bit slow today but let's get started um first set of announcements that I added are the release schedule for 127 is mostly finalized I've added some of that here um the release cycle

### Excerpt da transcript

hello everybody and welcome to the January 3rd 2023 iteration of the kubernetes Sig Windows uh community meeting as always these meetings are recorded and uploaded to YouTube so be sure to adhere to the cncf code of conduct um we're just coming off of some U.S holidays here so kind of might be a little bit slow today but let's get started um first set of announcements that I added are the release schedule for 127 is mostly finalized I've added some of that here um the release cycle officially begins next Monday um and next kind of important deadline is enhancements freeze which is next or uh on Thursday February 9th um it looks like targeting the April 11th for the 127 release um there's been a couple emails that went up to kubernetes Dev with more information if anybody is looking for that uh one other announcement is there is a release Team Shadow application that closes today if anybody's interested in shadowing any one of the release roles it's a good way to get involved with the release process and get to know more people there's a link to an email with more details if anybody's interested um just make sure to do that today before it closes does anybody have anything else they'd like to announce not we can um give some space if there's any new contributors I want to say hi looking at the attendee or participants list though I think everybody's already everybody knows everybody is um but if anybody wants to just feel free to say hi now we can go into some agenda items all right uh first agenda item James is a pull request yeah um sorry my voice lost my voice last week just getting it back um uh 122 is no longer supported and Fabian uh was able to get some of the PRS merged to be able to have a really good guide to getting started with process containers uh and so I want to get rid of all of the um Docker shim stuff that we had in there um it was uh using wins in kind of a couple different hacks uh enabled uh usage for that and so since that we don't really support Dr Shim anymore um and we have now a working host process container uh guide I was hoping to get rid of this so I just wanted to open it up and let folks know uh this is kind of been broken for a while because people are trying to use it with containerdy it didn't work and a bunch of stuff like that so um I think it'll just simplify a lot of this to not have it in there and avoid confusion so that means we'd no longer be making some of those the flannel images and things like that too right o
