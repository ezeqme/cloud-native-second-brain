---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Tutorials"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Mikkel Mørk Hegnhøj", "Melissa Klein", "Fermyon", "Ralph Squillace", "Microsoft"]
sched_url: https://kccncna2023.sched.com/event/1R2mE/tutorial-building-cloud-native-applications-using-webassembly-and-containers-mikkel-mork-hegnhoj-melissa-klein-fermyon-ralph-squillace-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Building+Cloud-Native+Applications+Using+WebAssembly+and+Containers+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Tutorial: Building Cloud-Native Applications Using WebAssembly and Containers - Mikkel Mørk Hegnhøj & Melissa Klein, Fermyon; Ralph Squillace, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Tutorials]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: United States / Chicago
- Speakers: Mikkel Mørk Hegnhøj, Melissa Klein, Fermyon, Ralph Squillace, Microsoft
- Schedule: https://kccncna2023.sched.com/event/1R2mE/tutorial-building-cloud-native-applications-using-webassembly-and-containers-mikkel-mork-hegnhoj-melissa-klein-fermyon-ralph-squillace-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Building+Cloud-Native+Applications+Using+WebAssembly+and+Containers+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Tutorial: Building Cloud-Native Applications Using WebAssembly and Containers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2mE/tutorial-building-cloud-native-applications-using-webassembly-and-containers-mikkel-mork-hegnhoj-melissa-klein-fermyon-ralph-squillace-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Building+Cloud-Native+Applications+Using+WebAssembly+and+Containers+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zvN9tuyqYow
- YouTube title: Tutorial: Building Cloud-Native Applications Using WebAssembly and Containers
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/tutorial-building-cloud-native-applications-using-webassembly-and-cont/zvN9tuyqYow.txt
- Transcript chars: 90646
- Keywords: assembly, container, running, application, actually, containers, basically, runtime, little, tutorial, docker, experience, dapper, cluster, wasm, everything, applications, module

### Resumo baseado na transcript

um I'm Ralph I'm I'm work for Microsoft I do Upstream stuff uh at Azure uh I report through AKs but I actually am part of the Upstream team and so I work uh partly on Upstream stuff like we my team is a team that handles all building of the kubernetes bits and the docker bits and things like that we give it to AKs and other services and if they have a problem we help fix it and then we're the ones that take the patch and bring

### Excerpt da transcript

um I'm Ralph I'm I'm work for Microsoft I do Upstream stuff uh at Azure uh I report through AKs but I actually am part of the Upstream team and so I work uh partly on Upstream stuff like we my team is a team that handles all building of the kubernetes bits and the docker bits and things like that we give it to AKs and other services and if they have a problem we help fix it and then we're the ones that take the patch and bring it back to the community and merge it upstream and so forth like that so that the service team can keep doing it its work uh my my my team uh was the team that built Helm 3 originally and the core unit of that is now Fon so the developers and uh everybody at Fon they part of their knowledge base especially with kubernetes but with um developer operational tools specifically uh Helm is one of those bases so they build count three um I was not only the PM for that which means I did nothing and they did everything um so and ml as a former colleague at Microsoft but in reality Mel is here along with Melissa representing F on their building spin so I want to sort of do a little back backstab for those and ml you're going to talk a little bit about web assembly and why we're doing that okay but just really quickly web assembly the reason we care about it is it's more like a cloud native binary as opposed to the metaphor of a container which is was supposed to be like a cloud native application but it really is a cloud native OS there's an entire file system in there in theory you could sort of crunch it down into a very small image but in reality what we've discovered is most people have very very limited time to get a feature up and running and so the containers tend to be very very large um in particular almost all the code that we wanted to Port into a container comes with like all kinds of dependencies and libraries and things like this and so you wanted to make your container very small but in reality a native application especially if it's something like python or JavaScript or just comes with reams of text and you would deploy them even if they didn't get invoked right and so it's really easy to have a container that's like without even thinking about it 700 megabytes 1.5 gigabytes and that was not the idea originally right the idea was we going to optimize this so the reason we like webm is because it's actually a mostly a binary format and so you really are in a module you really are shipping just the executable and any opin requi
