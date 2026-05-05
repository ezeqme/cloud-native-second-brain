---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "101 Track"
themes: ["101 Track"]
speakers: ["Mark Coleman", "Equinix Metal"]
sched_url: https://kccnceu2021.sched.com/event/iE55/taking-bare-metal-to-the-clouds-with-tinkerbell-mark-coleman-equinix-metal
youtube_search_url: https://www.youtube.com/results?search_query=Taking+Bare+Metal+to+the+Clouds+with+Tinkerbell+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Taking Bare Metal to the Clouds with Tinkerbell - Mark Coleman, Equinix Metal

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: Virtual / Virtual
- Speakers: Mark Coleman, Equinix Metal
- Schedule: https://kccnceu2021.sched.com/event/iE55/taking-bare-metal-to-the-clouds-with-tinkerbell-mark-coleman-equinix-metal
- Busca YouTube: https://www.youtube.com/results?search_query=Taking+Bare+Metal+to+the+Clouds+with+Tinkerbell+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Taking Bare Metal to the Clouds with Tinkerbell.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE55/taking-bare-metal-to-the-clouds-with-tinkerbell-mark-coleman-equinix-metal
- YouTube search: https://www.youtube.com/results?search_query=Taking+Bare+Metal+to+the+Clouds+with+Tinkerbell+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=L9yPdCqPcik
- YouTube title: Taking Bare Metal to the Clouds with Tinkerbell - Mark Coleman, Equinix Metal
- Match score: 0.857
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/taking-bare-metal-to-the-clouds-with-tinkerbell/L9yPdCqPcik.txt
- Transcript chars: 28759
- Keywords: tinkerbell, servers, server, running, hardware, operating, little, software, center, actions, public, around, essentially, actually, equinix, infrastructure, companies, whether

### Resumo baseado na transcript

okay welcome everybody to this talk at cubecon cloudnativecon europe 2021 virtual um despite having been involved with the cncf for four years this is actually the first time i'm speaking here so i'm very excited about it um so the title of today's talk is taking bare metal to the clouds with tinkerbell um and let's jump into what that's going to look like so i'll explain a little bit about myself um i think one of the questions a lot of people are going to have is why

### Excerpt da transcript

okay welcome everybody to this talk at cubecon cloudnativecon europe 2021 virtual um despite having been involved with the cncf for four years this is actually the first time i'm speaking here so i'm very excited about it um so the title of today's talk is taking bare metal to the clouds with tinkerbell um and let's jump into what that's going to look like so i'll explain a little bit about myself um i think one of the questions a lot of people are going to have is why would people be interested in running their own hardware anyway so i can share something around that assuming you do want to do that i want to explain how tinkerbell fits into the picture which is sometimes a little complex i'm going to look a little bit into why we decided to open source tinkerbell from equinix metal in the first place uh there's a lot of new exciting stuff in our zero five zero release that i'm gonna go through and then last but not least i'll talk about how people can get involved if they want to or if they want more information all right so a little bit about me i'm the senior director of developer relations equinix metal some of you may remember equinix metal as packet and up in the top right you can see this little logo that i really love which is the packet box with a sword riding on top of the equinix metal fortress um now i was involved in the cncf from 2016 until december 2020 and i put the little wink there because when speaking with priyanka she said i could call myself the cncf marketing chairperson emeritus for a little while i'm not quite sure how long that one's gonna last i live in north london and importantly for this talk until i started equinix medal i hadn't touched any hardware really since about 2001 when i was working on gaming pc and we're going to look at some of the things that i've learned in this talk so why are people interested in running their own hardware again well actually it's not again people always have been but i think there is the perception in some quarters that those companies still running their own infrastructure are what the crossing the chasm model would describe as laggards but this may not be as it seems um public cloud adoption has accelerated development of many technologies that help companies to change the way that they deploy software more easily kubernetes of course is an excellent example um but there are actually many reasons why people would be running on-prem hardware still and we're going to look at some of those now
