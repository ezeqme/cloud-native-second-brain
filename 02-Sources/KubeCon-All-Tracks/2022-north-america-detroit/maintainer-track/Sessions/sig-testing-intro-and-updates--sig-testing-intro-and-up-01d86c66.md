---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Benjamin Elder", "Michelle Shepardson", "Chao Dai", "Google", "Antonio Ojea Garcia", "Red Hat"]
sched_url: https://kccncna2022.sched.com/event/182Oe/sig-testing-intro-and-updates-benjamin-elder-michelle-shepardson-chao-dai-google-antonio-ojea-garcia-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Testing%3A+Intro+And+Updates+CNCF+KubeCon+2022
slides: []
status: parsed
---

# SIG Testing: Intro And Updates - Benjamin Elder & Michelle Shepardson & Chao Dai, Google; Antonio Ojea Garcia, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Benjamin Elder, Michelle Shepardson, Chao Dai, Google, Antonio Ojea Garcia, Red Hat
- Schedule: https://kccncna2022.sched.com/event/182Oe/sig-testing-intro-and-updates-benjamin-elder-michelle-shepardson-chao-dai-google-antonio-ojea-garcia-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Testing%3A+Intro+And+Updates+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre SIG Testing: Intro And Updates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Oe/sig-testing-intro-and-updates-benjamin-elder-michelle-shepardson-chao-dai-google-antonio-ojea-garcia-red-hat
- YouTube search: https://www.youtube.com/results?search_query=SIG+Testing%3A+Intro+And+Updates+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aXftW1MRxJ0
- YouTube title: SIG Testing: Intro and Updates - Mahamed Ali, Cisco
- Match score: 0.843
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/sig-testing-intro-and-updates/aXftW1MRxJ0.txt
- Transcript chars: 12251
- Keywords: testing, couple, framework, working, cluster, another, write, launch, program, allows, features, feature, google, particular, screen, everybody, projects, systems

### Resumo baseado na transcript

hi there everybody uh welcome to my talk uh I'll be giving a talk about s testing um intro and updates um all right my name is Muhammad I'm a senior devops engineer at Thousand Eyes by Cisco uh I am a kuties maintainer I um the S INF for Tech lead um I also work with s testing and S release on some projects I'm also a ctive maintainer another CNF incubating project I am the productivity working group lead there um I work similar similar concerns there as

### Excerpt da transcript

hi there everybody uh welcome to my talk uh I'll be giving a talk about s testing um intro and updates um all right my name is Muhammad I'm a senior devops engineer at Thousand Eyes by Cisco uh I am a kuties maintainer I um the S INF for Tech lead um I also work with s testing and S release on some projects I'm also a ctive maintainer another CNF incubating project I am the productivity working group lead there um I work similar similar concerns there as well um so a couple of topics I want to discuss today so I kind of want to me talk a bit more about SE testing what we do um some of the tools and systems that we have and some projects that we've been working on lately all right so what is s testing so we're interested in the effective testing of cuetes and automating Away a lot of toil that's related to testing very large code bases so we've got some Frameworks tools and infrastructure makes it very easy to write and run tests um in sure that commity is extremely stable and we develop and test that scale for us it's particularly important that we can track and detect flakes make sure they don't end up in releases um so leadership so we have three chairs um and we have five tech leads um so everybody's working on various different parts of the sck testing ecosystem all right so moving on to tools and systems so we've got a couple of tools that we've built so the first one is kind um kind is cuetes IND Docker it's a very powerful tool I'll talk about that in a second um another thing that we've got is keep test is a test framework that we build to launch test clusters for communties and the other thing we have is something called the ed test framework so it's a go program that we wrote that allows us to launch all sort of Ed tests and we have a couple of production systems that we use so the first one is prow that is the culated CI um you can go there and take a look at all the jobs that are running the health and status and the other thing we have is test grid which is a a grid of test results effectively um all so this is proud so um that's the address there proud.

case. uh these are jobs that run on there so it kind of looks something like that there's plenty of jobs and if you look at the time stamp on the left on the right you can see that we run quite a lot of jobs um there's like 10 jobs that I've scheduled within 2 minutes so this is what it looks like when you open a test um this particular test runs what we call the C ed3 on Google Cloud um so w
