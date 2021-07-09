
# Location Service Message Queue and gRPC Approach
Implementing a message queue for the create method of the location service would help to scale the system as the volume of users grows. 
Moving to and event driven architecture will allow the system to scale more effectively when receiving a high volume write (post) requests, helping to maintain a consistent and stable user experience.
The introduction of gRPC will provide an overall performance benefit to the service.

# The RESTful Approach
The existing code base does need some refactoring to make it more readable breaking out the services into separate files will improve the maintainability of the codes based and would make future service abstraction a lot easier. 
One future candidate to externalize into its own microservice could be the Connection Service, the Connection Service is the only service where there is significant business logic within the method; the other services are mainly pass through CRUD operations. Externalizing the Connection Service would ensure the general system CRUD operations are not impacted by the performance of the Connection Service.

# gRPC beyond the Location Service
Looking at the simplicity of the codebase and system, I would recommend that there is not enough significant evidence that would indicate that moving to gRPC is necessary. The following are a number of factors which play into the recommendation:

** As all the code lives in a single repo the complexity of integrating services at the time of deployment is significantly reduced. This would be reduced further through the adoption of TDD and automated test runs at the point of commit.
** The API's are not use by external partners or apps, this reduces the risk of API specs getting lost in translation / communication. This off sets the need for implementing gRPC which provides strong schema validation. 

There may be a case for gRPC in the future, but I do not currently think there is a case to refactor for the sake of it to introduce the technology approach. 