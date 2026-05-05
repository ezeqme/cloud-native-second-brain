---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Observability"
themes: ["Observability", "Sustainability"]
speakers: ["Nancy Chauhan", "Student", "Adriana Villela", "Dynatrace"]
sched_url: https://kccnceu2025.sched.com/event/1txEL/how-green-is-my-opentelemetry-collector-nancy-chauhan-student-adriana-villela-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=How+Green+Is+My+OpenTelemetry+Collector%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# How Green Is My OpenTelemetry Collector? - Nancy Chauhan, Student & Adriana Villela, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Sustainability]]
- País/cidade: United Kingdom / London
- Speakers: Nancy Chauhan, Student, Adriana Villela, Dynatrace
- Schedule: https://kccnceu2025.sched.com/event/1txEL/how-green-is-my-opentelemetry-collector-nancy-chauhan-student-adriana-villela-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=How+Green+Is+My+OpenTelemetry+Collector%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre How Green Is My OpenTelemetry Collector?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txEL/how-green-is-my-opentelemetry-collector-nancy-chauhan-student-adriana-villela-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=How+Green+Is+My+OpenTelemetry+Collector%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vWHeeV-a_YQ
- YouTube title: How Green is My OpenTelemetry Collector? - Nancy Chauhan
- Match score: 0.848
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/how-green-is-my-opentelemetry-collector/vWHeeV-a_YQ.txt
- Transcript chars: 23678
- Keywords: collector, basically, metrics, energy, kepler, collectors, operator, prometheus, memory, resource, environment, question, target, allocator, carbon, custom, resources, consumption

### Resumo baseado na transcript

She uh is a principal developer advocate at Dino Trace and she is an expert in open telemetry. Uh due to some issues uh she could not be here and we are going to miss you Adriana. a problem there was a the question was by developers and operators like for all those people who are new to open telemetry the question was that why can't we have an open standard that supports the traces metrics and logs and work for all the vendors and due to this question to answer this question open telemetry was born uh to provide a single set of SDKs uh to have a standard format and support for traces metrics and logs so um how about we start with collect collector Now open telemetry is a vendor neutral agent which is used to ingest uh as you can see the receiver we have the uh open telemetry receiver hostmetrics receiver Kafka receiver and then we have a processing. For our presentation we are just going to focus on the collector which is deployed on kubernetes but uh before this we are going to understand that what exactly operator does because uh collector deployed on kubernetus is managed by operator.

### Excerpt da transcript

Awesome. So we can start. Thank you so much uh for coming for the session. Uh how green is my open telemetry collector. So uh I was about to present this talk with Adriana. She's amazing. She uh is a principal developer advocate at Dino Trace and she is an expert in open telemetry. I wish she could be here. Uh due to some issues uh she could not be here and we are going to miss you Adriana. Uh a little bit about me. I am Nancy. I am a CNCF ambassador. I also I was a part of tag environment sustainability which is all about sustainability in tech. And uh with this I worked as devops engineer. Then I worked as developer advocate with gitport and local stack. And uh other than work I love cats. I love traveling. I also love making illustrations. So that's about me. Uh you can scan the QR code to know more about me or get connected with me. So let's get started. uh global warming is real. Uh I just want to ask like can you just raise hands? Do you think this is true? Like whether it's about the rising sea level, whether it's about the climate change, the drastic changes, uh we know that it's for real.

Um I have a question for you in the audience. Does anyone know that which country is moving its capital city due to climate change concern? Any guess? >> Indonesia. >> That's true. Indonesia. So Indonesia is moving its capital city Jakarta to a new capital city due to climate change and this is concerning. It's a huge thing if if a whole country has to move its capital due to rising sea level. Uh then what what percentage of global carbon emission is the IT sector responsible for? Well the number is 2% global 2% of global carbon emissions. It looks like a small number but the catch is it's going to increase by 12% by 2040 and this is a huge number. So we as an engineer are responsible for this and then that's bring us the question that how tech and environment are correlated. So we know that IT sector is responsible for 2% of global carbon emissions and it's going to increase in future. Then data centers rank in the top 10 of water consuming industrial or commercial industries. Um they this applies to both uh indirectly to generate the electricity that the data centers need to operate and directly as a liquid coolant to dissipate the heat generated.

So it's a huge so so it's a huge it's a significant numbers and then keeping our systems observable has an impact on the environment like whatever tech we are running on the cloud everything has an impact and that's
