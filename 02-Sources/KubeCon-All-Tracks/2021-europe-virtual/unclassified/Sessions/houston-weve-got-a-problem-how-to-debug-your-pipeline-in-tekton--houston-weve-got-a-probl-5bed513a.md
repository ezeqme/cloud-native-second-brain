---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Unclassified"
themes: ["Cloud Native"]
speakers: ["Vibhav Bobade", "Vincent Demeester", "Red Hat"]
sched_url: https://kccnceu2021.sched.com/event/iE3O/houston-weve-got-a-problem-how-to-debug-your-pipeline-in-tekton-vibhav-bobade-vincent-demeester-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Houston%2C+We%E2%80%99ve+Got+a+Problem%21+%3A+How+to+Debug+your+Pipeline+in+Tekton+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Houston, We’ve Got a Problem! : How to Debug your Pipeline in Tekton - Vibhav Bobade & Vincent Demeester, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Unclassified]]
- Temas: [[Cloud Native]]
- País/cidade: Virtual / Virtual
- Speakers: Vibhav Bobade, Vincent Demeester, Red Hat
- Schedule: https://kccnceu2021.sched.com/event/iE3O/houston-weve-got-a-problem-how-to-debug-your-pipeline-in-tekton-vibhav-bobade-vincent-demeester-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Houston%2C+We%E2%80%99ve+Got+a+Problem%21+%3A+How+to+Debug+your+Pipeline+in+Tekton+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Houston, We’ve Got a Problem! : How to Debug your Pipeline in Tekton.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE3O/houston-weve-got-a-problem-how-to-debug-your-pipeline-in-tekton-vibhav-bobade-vincent-demeester-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Houston%2C+We%E2%80%99ve+Got+a+Problem%21+%3A+How+to+Debug+your+Pipeline+in+Tekton+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qjY2Df-Po-g
- YouTube title: Houston, We’ve Got a Problem! : How to Debug your Pipeline in... Vibhav Bobade & Vincent Demeester
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/houston-weve-got-a-problem-how-to-debug-your-pipeline-in-tekton/qjY2Df-Po-g.txt
- Transcript chars: 28056
- Keywords: pipeline, pipelines, running, failure, tecton, inside, container, debugging, itself, failed, success, probably, environment, provide, actually, little, basically, continue

### Resumo baseado na transcript

all right um welcome to this talk uh houston we've got a problem how to debug your pipeline in tecton uh i'm vincent demister principal software senior principal software engineer red and i am one of the leader of the techdown project um i also worked very hard and i work on load checking stuff and technon as well and yeah today we are going to talk about how to debug your pipeline uh right so let's go through the agenda um first we'll define a little bit what do

### Excerpt da transcript

all right um welcome to this talk uh houston we've got a problem how to debug your pipeline in tecton uh i'm vincent demister principal software senior principal software engineer red and i am one of the leader of the techdown project um i also worked very hard and i work on load checking stuff and technon as well and yeah today we are going to talk about how to debug your pipeline uh right so let's go through the agenda um first we'll define a little bit what do we mean by debug in debug what uh then we'll go rather quickly on what is takedown in tekton in a nutshell hopefully you know already a bit what is takedown when going to this talk but if you don't uh this will be a really quick introduction to tectum then uh we'll do a little bit of magic in russian dolls explaining how all this works uh then the bob will do a demo and and we'll finish with the next steps after after after this demo after this work what will be the next steps so first debug what so um let's talk a little bit about about debugging so uh debugging is the process of identifying and removing errors from computer hardware and software and in this case so we will be talking about debugging but it will be in terms of pipelines so and debugging pipelines themselves so what do i mean by when like debugging pipelines and what are pipelines so pipelines uh pipelines usually is a liner leaner liner linear sequence of specialized model used for pipelining uh basically this means uh you do a task uh or an action then an election then another action and some can be in sequence some can be impressed there's a lot of types of pipeliners that are pipeliners even pipeline there's a lot of type of pipeline in our context in the context of this talk we're mainly talking about cicd pipelines and in our example is more accurately be useful in a continuous integration pipeline but yeah we will focus on the ci cd pipelines uh but this could probably apply to other type of pipeline that can be done inside texan if we wanted to yeah so why would we ever want to debug our pipelines now if there is a pipeline which works on your machine but not on the ci it's very hard to understand why it's not working on the ci because you would need to understand what is the environment uh the pipeline is running in and that would be the ci environment and you would need to get access to the ci environment and understand this thing so uh debugging pipelines could be helpful in this way where you just get access to the ci
