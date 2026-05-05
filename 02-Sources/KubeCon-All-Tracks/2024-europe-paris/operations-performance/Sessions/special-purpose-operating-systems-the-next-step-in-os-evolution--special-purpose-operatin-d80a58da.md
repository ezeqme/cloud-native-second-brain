---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Danielle Tal", "Microsoft", "Felipe Huici", "Unikraft GmbH", "Sean McGinnis", "Lambda", "Mauro Morales", "Spectro Cloud", "Justin Haynes", "Google"]
sched_url: https://kccnceu2024.sched.com/event/1YeSR/special-purpose-operating-systems-the-next-step-in-os-evolution-or-one-trick-ponies-danielle-tal-microsoft-felipe-huici-unikraft-gmbh-sean-mcginnis-lambda-mauro-morales-spectro-cloud-justin-haynes-google
youtube_search_url: https://www.youtube.com/results?search_query=Special+Purpose+Operating+Systems%3A+The+Next+Step+in+OS+Evolution+or+One-Trick+Ponies%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Special Purpose Operating Systems: The Next Step in OS Evolution or One-Trick Ponies? - Danielle Tal, Microsoft; Felipe Huici, Unikraft GmbH; Sean McGinnis, Lambda; Mauro Morales, Spectro Cloud; Justin Haynes, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Danielle Tal, Microsoft, Felipe Huici, Unikraft GmbH, Sean McGinnis, Lambda, Mauro Morales, Spectro Cloud, Justin Haynes, Google
- Schedule: https://kccnceu2024.sched.com/event/1YeSR/special-purpose-operating-systems-the-next-step-in-os-evolution-or-one-trick-ponies-danielle-tal-microsoft-felipe-huici-unikraft-gmbh-sean-mcginnis-lambda-mauro-morales-spectro-cloud-justin-haynes-google
- Busca YouTube: https://www.youtube.com/results?search_query=Special+Purpose+Operating+Systems%3A+The+Next+Step+in+OS+Evolution+or+One-Trick+Ponies%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Special Purpose Operating Systems: The Next Step in OS Evolution or One-Trick Ponies?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSR/special-purpose-operating-systems-the-next-step-in-os-evolution-or-one-trick-ponies-danielle-tal-microsoft-felipe-huici-unikraft-gmbh-sean-mcginnis-lambda-mauro-morales-spectro-cloud-justin-haynes-google
- YouTube search: https://www.youtube.com/results?search_query=Special+Purpose+Operating+Systems%3A+The+Next+Step+in+OS+Evolution+or+One-Trick+Ponies%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uD-T9LdfvrM
- YouTube title: Special Purpose Operating Systems: The Next Step in OS Evolution or One-Trick Ponies?
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/special-purpose-operating-systems-the-next-step-in-os-evolution-or-one/uD-T9LdfvrM.txt
- Transcript chars: 30774
- Keywords: operating, special, purpose, container, systems, working, running, containers, specialized, actually, little, rocket, unicraft, virtual, talking, docker, question, already

### Resumo baseado na transcript

all right let's get started hello and welcome to the final day of cubec con U 2024 in the afternoon and we're we're amazed that so many of you made it here this is the um special purpose operating system working group panel of the tag runtime um and uh without further Ado um I will have the participants introduce themselves please go ahead Shan all right I I'm Sean mcginness uh I am a former maintainer of the B rocket project um currently working at Lambda Labs but still

### Excerpt da transcript

all right let's get started hello and welcome to the final day of cubec con U 2024 in the afternoon and we're we're amazed that so many of you made it here this is the um special purpose operating system working group panel of the tag runtime um and uh without further Ado um I will have the participants introduce themselves please go ahead Shan all right I I'm Sean mcginness uh I am a former maintainer of the B rocket project um currently working at Lambda Labs but still a special purpose operating system Enthusiast my name is Justin Haynes uh I'm at Google right now working on their container oper optimized operating system that underpins gke uh and before that I worked on bottle rocket hi everyone my name is Mao Morales I work for spectr cloud and I'm currently a maintainer at kyus hi everybody my name is Philipi I'm one of the creators and maintainers of unicraft the unical project and more recently CEO and co-founder of uh a company that's building a new Cloud platform based on unicel called craft Cloud hey gentlemen and maybe two ladies I spotted in the crowd um my name is Danielle tal I work at Microsoft and PM for flat car and I'm also chairing co-chairing the tag runtime and maybe our lovely host here would want to introduce himself too hi I'm T I also work for Microsoft um today I'm trying to have no project affiliations because that will make two of us and that wouldn't work out all right the way this P the way we want this panel to work is we want your participation so if you have any um remarks or questions or just want to stop us bubbling and bring something in yourself please raise your hand we have um assistant in the back that he'll find you with his mic and then he'll you'll be part of this discussion all right um so in this Spirit let's let's get things started what for you would be a special purpose operating system did you come here with any idea anyone there there is an idea of course uh immutable and of course uh usable also not only as a kubernetes node but also for special purposes think of an edge deployment without the need for a full kubernetes cluster but with a container run time like podman or something like that uh but always with the purpose of running containers of course everything is a container everything is possible that's a good opinion we may have a surprise for you later uh any other opinions oh I'll I'll maybe something running at the edge or something running like with low resources so good input it's great to get
