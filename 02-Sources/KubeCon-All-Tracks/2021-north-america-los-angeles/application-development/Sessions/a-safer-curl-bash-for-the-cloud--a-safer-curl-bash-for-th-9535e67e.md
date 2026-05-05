---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Application + Development"
themes: ["Application + Development"]
speakers: ["Carolyn Van Slyck", "Microsoft"]
sched_url: https://kccncna2021.sched.com/event/lV2O/a-safer-curl-bash-for-the-cloud-carolyn-van-slyck-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=A+Safer+Curl+%7C+Bash+for+the+Cloud+CNCF+KubeCon+2021
slides: []
status: parsed
---

# A Safer Curl | Bash for the Cloud - Carolyn Van Slyck, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Application + Development]]
- Temas: [[Application + Development]]
- País/cidade: United States / Los Angeles
- Speakers: Carolyn Van Slyck, Microsoft
- Schedule: https://kccncna2021.sched.com/event/lV2O/a-safer-curl-bash-for-the-cloud-carolyn-van-slyck-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=A+Safer+Curl+%7C+Bash+for+the+Cloud+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre A Safer Curl | Bash for the Cloud.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV2O/a-safer-curl-bash-for-the-cloud-carolyn-van-slyck-microsoft
- YouTube search: https://www.youtube.com/results?search_query=A+Safer+Curl+%7C+Bash+for+the+Cloud+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hLQC-Sfy0NI
- YouTube title: A Safer Curl | Bash for the Cloud - Carolyn Van Slyck, Microsoft
- Match score: 0.769
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/a-safer-curl-bash-for-the-cloud/hLQC-Sfy0NI.txt
- Transcript chars: 19646
- Keywords: bundle, porter, install, installation, script, credentials, software, command, bundles, laptop, installed, inside, installer, experience, database, running, instead, security

### Resumo baseado na transcript

hi i'm carolyn van slick a principal software engineer at microsoft today i want to think through how we can have our cake and eat it too namely i want to install software quickly and securely now i have to admit that i'm kind of a sucker for running an installation script by using curl pipe bash i mean i know i shouldn't but it's just so easy and i'm so lazy now this laziness extends beyond just installing devtools on my laptop a lot of cloud native software could

### Excerpt da transcript

hi i'm carolyn van slick a principal software engineer at microsoft today i want to think through how we can have our cake and eat it too namely i want to install software quickly and securely now i have to admit that i'm kind of a sucker for running an installation script by using curl pipe bash i mean i know i shouldn't but it's just so easy and i'm so lazy now this laziness extends beyond just installing devtools on my laptop a lot of cloud native software could benefit from having a more straightforward installation process common wisdom says that curling a script piping its bash isn't safe so what can we do to make this work instead what if we could make installers that are as easy to use as curl pipe bash but we're a whole lot safer first let's talk about what curl pipe bash really is so this is what it looks like that's when you copy and paste a command that looks like the one right here now we all use scripts like this because they install quickly and it helps you a software that you aren't familiar with curl downloads the script and then the script contents are piped to bash and they're immediately executed personally i really like installation scripts i can copy paste my way to victory with just a single command they require little to no knowledge of the installation logic or tooling and yeah i really do believe that the project maintainers can automate the installation way better than me on the first try so let's review why curl pipe bash is a security risk what if someone on the internet offered to help install an application that you really wanted and they would do it for you all you need is to hand over your laptop for five seconds and they'll type super fast and boom it's installed now i don't know about you but i don't hand over my laptop to my husband and i trust him mostly when we think about handing over your laptop to a stranger it's easy to see why it's risky they would have access to everything on there documents pictures environment variables with security tokens and passwords you're logged into a bunch of sites maybe even your work vpn it's clear that they could do anything with your laptop that you could do and that doesn't change when you switch from a physical laptop to a quick copy paste of an installation script when you use magic installation scripts you are giving the script full access to your laptop and anything your laptop has access to oops so okay what if you read the script first and then run it you open the script in y
