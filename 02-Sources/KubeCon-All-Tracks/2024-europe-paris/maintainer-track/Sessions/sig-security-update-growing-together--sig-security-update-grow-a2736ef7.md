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
themes: ["AI ML", "Security", "Storage Data", "Community Governance"]
speakers: ["Ian Coldwater", "Independent", "Tabitha Sable", "Datadog", "Mahé Tardy", "Isovalent", "Rory McCune", "Datadog"]
sched_url: https://kccnceu2024.sched.com/event/1YhiH/sig-security-update-growing-together-ian-coldwater-independent-tabitha-sable-datadogmahe-tardy-isovalent-rory-mccune-datadog
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Security+Update%3A+Growing+Together+CNCF+KubeCon+2024
slides: []
status: parsed
---

# SIG Security Update: Growing Together - Ian Coldwater, Independent; Tabitha Sable, Datadog;Mahé Tardy, Isovalent; Rory McCune, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Storage Data]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Ian Coldwater, Independent, Tabitha Sable, Datadog, Mahé Tardy, Isovalent, Rory McCune, Datadog
- Schedule: https://kccnceu2024.sched.com/event/1YhiH/sig-security-update-growing-together-ian-coldwater-independent-tabitha-sable-datadogmahe-tardy-isovalent-rory-mccune-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Security+Update%3A+Growing+Together+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre SIG Security Update: Growing Together.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhiH/sig-security-update-growing-together-ian-coldwater-independent-tabitha-sable-datadogmahe-tardy-isovalent-rory-mccune-datadog
- YouTube search: https://www.youtube.com/results?search_query=SIG+Security+Update%3A+Growing+Together+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4TYjaI0tBBM
- YouTube title: SIG Security Update: Growing Together
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sig-security-update-growing-together/4TYjaI0tBBM.txt
- Transcript chars: 30888
- Keywords: security, together, working, projects, meeting, happen, actually, started, policy, tooling, process, admission, assessments, everybody, contributors, experience, threat, involved

### Resumo baseado na transcript

all right hi my name is Ian Coldwater I am co-chair of kubernetes Sig security this is Sig security growing together our maintainer track talk if you are in here for a different talk you are in the wrong room and that's cool we're happy to hang out with you anyway what is Sig security Sig security is uh um kubernetes Sig that takes a community- building approach to improving kubernetes security um based on the principle of people coming together and consent um we work to improve security for started out at as the thirdparty um audit working group for the first audit several years ago now um there was a working group that got together and um for those who are less familiar with kubernetes governance structures working groups are temporary um they are supposed to be there to do one thing and then disband the thing is that we actually needed as it turns out more than one security audit over time and so that was going to need to be a thing that would need to and whatever it is if you have an idea of something in kubernetes that could be improved in some way if you have an idea of something that seems really interesting or weird that you want to learn about something that you want to make happen a really cool hack you heard about that you want to share whatever it is we would love to see you so come on out um we have s- Security in kubernetes slack if you want to come meet us on...

### Excerpt da transcript

all right hi my name is Ian Coldwater I am co-chair of kubernetes Sig security this is Sig security growing together our maintainer track talk if you are in here for a different talk you are in the wrong room and that's cool we're happy to hang out with you anyway what is Sig security Sig security is uh um kubernetes Sig that takes a community- building approach to improving kubernetes security um based on the principle of people coming together and consent um we work to improve security for the project itself as well as our end users by cultivating a space where security-minded contributors of all experience levels can get together bring their energy and ideas and work together across sigs and internally to help make kubernetes more secure a lot of our work is done in our sub projects we've got four of them right now um we've got six security docs which works on improving the documentation content and creating new content um so that people can get good guidance on how to use kubernetes securely we've got Sig security tooling which develops and maintains security features for internal kubernetes development we've got security self assessments which empowers projects under the kubernetes banner to improve their own security by teaching them how to threat model for themselves and we've got Sig security audit which is responsible for the periodic thirdparty external audits of kubernetes security that happen every once in a while we'll be hearing from all of these sub projects in a minute all of these things help keep kubernetes security improving over time so first off we're going to be hearing from six security toing hi everyone hi May so I'm very glad to say that I've been involved in six security for a few years now and today I will be representing six security tooling oh thank you so um six security tooling improves kubernetes security by writing codes mainly and we maintain mostly two projects so the first one is the auto refreshing cve feed so this is like an official list of kubernetes CV um from the website for kubernetes and uh those have been uh very helpful to help people maintaining cluster to keep them secured in the past so now it's in beta stage uh it's going to graduate into stable and the next project is like the scanning of the kubernetes release artifact so basically we scan the kubernetes container image and the binaries to find if there are any known issues uh that we in them so uh wanted to mention that the SE security tooling is meeting
