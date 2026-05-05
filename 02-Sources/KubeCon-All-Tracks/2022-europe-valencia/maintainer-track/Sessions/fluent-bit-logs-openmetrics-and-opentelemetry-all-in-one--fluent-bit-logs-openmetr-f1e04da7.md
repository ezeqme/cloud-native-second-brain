---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Eduardo Silva", "Anurag Gupta", "Calyptia"]
sched_url: https://kccnceu2022.sched.com/event/ytl1/fluent-bit-logs-openmetrics-and-opentelemetry-all-in-one-eduardo-silva-anurag-gupta-calyptia
youtube_search_url: https://www.youtube.com/results?search_query=Fluent+Bit%3A+Logs%2C+OpenMetrics%2C+and+OpenTelemetry+all-in-one+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Fluent Bit: Logs, OpenMetrics, and OpenTelemetry all-in-one - Eduardo Silva & Anurag Gupta, Calyptia

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Eduardo Silva, Anurag Gupta, Calyptia
- Schedule: https://kccnceu2022.sched.com/event/ytl1/fluent-bit-logs-openmetrics-and-opentelemetry-all-in-one-eduardo-silva-anurag-gupta-calyptia
- Busca YouTube: https://www.youtube.com/results?search_query=Fluent+Bit%3A+Logs%2C+OpenMetrics%2C+and+OpenTelemetry+all-in-one+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Fluent Bit: Logs, OpenMetrics, and OpenTelemetry all-in-one.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytl1/fluent-bit-logs-openmetrics-and-opentelemetry-all-in-one-eduardo-silva-anurag-gupta-calyptia
- YouTube search: https://www.youtube.com/results?search_query=Fluent+Bit%3A+Logs%2C+OpenMetrics%2C+and+OpenTelemetry+all-in-one+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TciIQVve2V0
- YouTube title: Fluent Bit: Logs, OpenMetrics, and OpenTelemetry all-in-one - Eduardo Silva & Anurag Gupta, Calyptia
- Match score: 0.837
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/fluent-bit-logs-openmetrics-and-opentelemetry-all-in-one/TciIQVve2V0.txt
- Transcript chars: 32050
- Keywords: fluent, metrics, traces, logs, prometheus, started, ecosystem, already, output, question, support, exporter, always, performance, information, collect, standard, course

### Resumo baseado na transcript

hello hi guys how are you good happy to come back at cubecon who's your first time here maybe you can raise your hand oh really oh man that's great that's great in the meanwhile they bring all the audio stuff so we're going to do some quick in conversation so well first of all welcome i think that kubecon is one of the best conference around not because of just kubernetes because of technology and and community so yeah really happy to hear that this is the first time more than just hdp and then on of course on top of that all of the tracing side as part of part of the roadmap which we'll cover here in a bit so what does this look like in actuality uh when we put it all together so we have a quick demo and this is very very simple i have a javascript application i'm instrumenting it with the standard of the day which is open telemetry all the great work that that team's done for building those libraries we

### Excerpt da transcript

hello hi guys how are you good happy to come back at cubecon who's your first time here maybe you can raise your hand oh really oh man that's great that's great in the meanwhile they bring all the audio stuff so we're going to do some quick in conversation so well first of all welcome i think that kubecon is one of the best conference around not because of just kubernetes because of technology and and community so yeah really happy to hear that this is the first time that everybody raised the hand yeah that's awesome okay okay maybe some question who's a fluency or fluent bet user already okay now who's interested in metrics okay there you have yeah let's get started is this working too yeah oh awesome okay so yeah hey everyone my name is honorag i'm one of the co-founders maintainers fluent d flint bit project and of course we have eduardo creator of the flintfit project as well so yeah really when we start looking at fluent bit and fluentd the way we've begun to think about these projects is really a swiss army knife for observability how do we look at all this data start slicing and dicing it making it very accessible as part of the ecosystem and how these projects start to fit together kind of in the in the broader set of the ecosystem right many folks first time at cubecon so many projects going around how do we look at this ecosystem at a little bit of a broader level so one of the important things is like a when you are thinking about observability in general it's because you want to analyze you know your application how this stuff is working right at the end of the day managing infrastructure or managing the services that run behind the scenes you don't want to be worried about that right it's like if you're using a linux system you don't want to know how glfc is working right you just want to make sure that the application is running it's getting the right resources memory allocation everything and if we go to a higher level from observability your final goal always will be how do i analyze my data right but in order to analyze your data you need to get the data first right in a central place most of the time and this data that you get come from different sources and from different kind of natures right you can think about logs you can think about metrics and you can think about traces i i i guess that most of you already working in in some companies and i'm pretty sure that 99 of you will say we don't have just one solution for everything right y
