from antlr.JavaParser import JavaParser

from agents.JavaAgentBase import JavaRefactorAgent

class JavaLogAgent(JavaRefactorAgent):
  @staticmethod
  def addOptions(parser):
    parser.add_argument(
        '--method-declaration',
        help='Specify the method declarition name, e.g. `--method-declaration '
             'func would log inside the statments inside func declaration')
    parser.add_argument(
        '--each-line', action='store_true', default=False,
        help='Add logging in between each statement')
    parser.add_argument('--method-invocation',
        help='Specify the method invocation name,'
              'e.g. `--method-invocation func` would log every func() call')
    parser.add_argument(
        '--tag', help='Specify the tag used for logging')

  def actions(self):
    # Log every line
    if self.args.method_declaration:
      self.refactor.ActionOnX(
          self.tb, JavaParser.MethodDeclarationContext,
          condition_fn = lambda x: x.IDENTIFIER == self.args.method_declaration,
          action_fn = self.logEveryLine)
    if self.args.method_invocation:
      self.refactor.ActionOnX(
          self.tb, JavaParser.MethodDeclarationContext,
          condition_fn = lambda x: x.IDENTIFIER == self.args.method_invocation,
          action_fn = self.logInvocation)

  def logEveryLine(self, token):
    import ipdb
    ipdb.set_trace()

  def logInvocation(self, token):
    import ipdb
    ipdb.set_trace()


class JavaTraceAgent(JavaRefactorAgent):
  @staticmethod
  def addOptions(parser):
    parser.add_argument(
        '--method-declaration',
        help='Specify the method declarition name, e.g. `--method-declaration '
             'func would trace inside the statments inside func declaration')
    parser.add_argument(
        '--each-line', action='store_true', default=False,
        help='Add tracing in between each statement')
    parser.add_argument('--method-invocation',
        help='Specify the method invocation name,'
              'e.g. `--method-invocation func` would tracing every func() call')

  def actions(self):
    # Trace every line
    if self.args.method_declaration:
      self.refactor.ActionOnX(
          self.tb, JavaParser.MethodDeclarationContext,
          condition_fn = lambda x: x.IDENTIFIER == self.args.method_declaration,
          action_fn = self.traceEveryLine)
    if self.args.method_invocation:
      self.refactor.ActionOnX(
          self.tb, JavaParser.MethodDeclarationContext,
          condition_fn = lambda x: x.IDENTIFIER == self.args.method_invocation,
          action_fn = self.traceInvocation)

  def traceEveryLine(self, token):
    import ipdb
    ipdb.set_trace()

  def traceInvocation(self, token):
    import ipdb
    ipdb.set_trace()

class JavaStats(JavaAgentBase):
  # Enter a parse tree produced by JavaParser#compilationUnit.
  def enterCompilationUnit(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#compilationUnit.
  def exitCompilationUnit(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#packageDeclaration.
  def enterPackageDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#packageDeclaration.
  def exitPackageDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#importDeclaration.
  def enterImportDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#importDeclaration.
  def exitImportDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#typeDeclaration.
  def enterTypeDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#typeDeclaration.
  def exitTypeDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#modifier.
  def enterModifier(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#modifier.
  def exitModifier(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#classOrInterfaceModifier.
  def enterClassOrInterfaceModifier(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#classOrInterfaceModifier.
  def exitClassOrInterfaceModifier(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#variableModifier.
  def enterVariableModifier(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#variableModifier.
  def exitVariableModifier(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#classDeclaration.
  def enterClassDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#classDeclaration.
  def exitClassDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#typeParameters.
  def enterTypeParameters(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#typeParameters.
  def exitTypeParameters(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#typeParameter.
  def enterTypeParameter(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#typeParameter.
  def exitTypeParameter(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#typeBound.
  def enterTypeBound(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#typeBound.
  def exitTypeBound(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#enumDeclaration.
  def enterEnumDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#enumDeclaration.
  def exitEnumDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#enumConstants.
  def enterEnumConstants(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#enumConstants.
  def exitEnumConstants(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#enumConstant.
  def enterEnumConstant(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#enumConstant.
  def exitEnumConstant(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#enumBodyDeclarations.
  def enterEnumBodyDeclarations(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#enumBodyDeclarations.
  def exitEnumBodyDeclarations(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#interfaceDeclaration.
  def enterInterfaceDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#interfaceDeclaration.
  def exitInterfaceDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#classBody.
  def enterClassBody(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#classBody.
  def exitClassBody(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#interfaceBody.
  def enterInterfaceBody(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#interfaceBody.
  def exitInterfaceBody(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#classBodyDeclaration.
  def enterClassBodyDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#classBodyDeclaration.
  def exitClassBodyDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#memberDeclaration.
  def enterMemberDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#memberDeclaration.
  def exitMemberDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#methodDeclaration.
  def enterMethodDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#methodDeclaration.
  def exitMethodDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#methodBody.
  def enterMethodBody(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#methodBody.
  def exitMethodBody(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#typeTypeOrVoid.
  def enterTypeTypeOrVoid(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#typeTypeOrVoid.
  def exitTypeTypeOrVoid(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#genericMethodDeclaration.
  def enterGenericMethodDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#genericMethodDeclaration.
  def exitGenericMethodDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#genericConstructorDeclaration.
  def enterGenericConstructorDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#genericConstructorDeclaration.
  def exitGenericConstructorDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#constructorDeclaration.
  def enterConstructorDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#constructorDeclaration.
  def exitConstructorDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#fieldDeclaration.
  def enterFieldDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#fieldDeclaration.
  def exitFieldDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#interfaceBodyDeclaration.
  def enterInterfaceBodyDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#interfaceBodyDeclaration.
  def exitInterfaceBodyDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#interfaceMemberDeclaration.
  def enterInterfaceMemberDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#interfaceMemberDeclaration.
  def exitInterfaceMemberDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#constDeclaration.
  def enterConstDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#constDeclaration.
  def exitConstDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#constantDeclarator.
  def enterConstantDeclarator(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#constantDeclarator.
  def exitConstantDeclarator(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#interfaceMethodDeclaration.
  def enterInterfaceMethodDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#interfaceMethodDeclaration.
  def exitInterfaceMethodDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#interfaceMethodModifier.
  def enterInterfaceMethodModifier(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#interfaceMethodModifier.
  def exitInterfaceMethodModifier(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#genericInterfaceMethodDeclaration.
  def enterGenericInterfaceMethodDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#genericInterfaceMethodDeclaration.
  def exitGenericInterfaceMethodDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#variableDeclarators.
  def enterVariableDeclarators(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#variableDeclarators.
  def exitVariableDeclarators(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#variableDeclarator.
  def enterVariableDeclarator(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#variableDeclarator.
  def exitVariableDeclarator(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#variableDeclaratorId.
  def enterVariableDeclaratorId(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#variableDeclaratorId.
  def exitVariableDeclaratorId(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#variableInitializer.
  def enterVariableInitializer(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#variableInitializer.
  def exitVariableInitializer(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#arrayInitializer.
  def enterArrayInitializer(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#arrayInitializer.
  def exitArrayInitializer(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#classOrInterfaceType.
  def enterClassOrInterfaceType(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#classOrInterfaceType.
  def exitClassOrInterfaceType(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#typeArgument.
  def enterTypeArgument(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#typeArgument.
  def exitTypeArgument(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#qualifiedNameList.
  def enterQualifiedNameList(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#qualifiedNameList.
  def exitQualifiedNameList(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#formalParameters.
  def enterFormalParameters(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#formalParameters.
  def exitFormalParameters(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#formalParameterList.
  def enterFormalParameterList(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#formalParameterList.
  def exitFormalParameterList(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#formalParameter.
  def enterFormalParameter(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#formalParameter.
  def exitFormalParameter(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#lastFormalParameter.
  def enterLastFormalParameter(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#lastFormalParameter.
  def exitLastFormalParameter(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#qualifiedName.
  def enterQualifiedName(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#qualifiedName.
  def exitQualifiedName(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#literal.
  def enterLiteral(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#literal.
  def exitLiteral(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#integerLiteral.
  def enterIntegerLiteral(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#integerLiteral.
  def exitIntegerLiteral(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#floatLiteral.
  def enterFloatLiteral(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#floatLiteral.
  def exitFloatLiteral(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#annotation.
  def enterAnnotation(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#annotation.
  def exitAnnotation(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#elementValuePairs.
  def enterElementValuePairs(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#elementValuePairs.
  def exitElementValuePairs(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#elementValuePair.
  def enterElementValuePair(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#elementValuePair.
  def exitElementValuePair(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#elementValue.
  def enterElementValue(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#elementValue.
  def exitElementValue(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#elementValueArrayInitializer.
  def enterElementValueArrayInitializer(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#elementValueArrayInitializer.
  def exitElementValueArrayInitializer(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#annotationTypeDeclaration.
  def enterAnnotationTypeDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#annotationTypeDeclaration.
  def exitAnnotationTypeDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#annotationTypeBody.
  def enterAnnotationTypeBody(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#annotationTypeBody.
  def exitAnnotationTypeBody(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#annotationTypeElementDeclaration.
  def enterAnnotationTypeElementDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#annotationTypeElementDeclaration.
  def exitAnnotationTypeElementDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#annotationTypeElementRest.
  def enterAnnotationTypeElementRest(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#annotationTypeElementRest.
  def exitAnnotationTypeElementRest(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#annotationMethodOrConstantRest.
  def enterAnnotationMethodOrConstantRest(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#annotationMethodOrConstantRest.
  def exitAnnotationMethodOrConstantRest(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#annotationMethodRest.
  def enterAnnotationMethodRest(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#annotationMethodRest.
  def exitAnnotationMethodRest(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#annotationConstantRest.
  def enterAnnotationConstantRest(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#annotationConstantRest.
  def exitAnnotationConstantRest(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#defaultValue.
  def enterDefaultValue(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#defaultValue.
  def exitDefaultValue(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#block.
  def enterBlock(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#block.
  def exitBlock(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#blockStatement.
  def enterBlockStatement(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#blockStatement.
  def exitBlockStatement(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#localVariableDeclaration.
  def enterLocalVariableDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#localVariableDeclaration.
  def exitLocalVariableDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#localTypeDeclaration.
  def enterLocalTypeDeclaration(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#localTypeDeclaration.
  def exitLocalTypeDeclaration(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#statement.
  def enterStatement(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#statement.
  def exitStatement(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#catchClause.
  def enterCatchClause(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#catchClause.
  def exitCatchClause(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#catchType.
  def enterCatchType(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#catchType.
  def exitCatchType(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#finallyBlock.
  def enterFinallyBlock(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#finallyBlock.
  def exitFinallyBlock(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#resourceSpecification.
  def enterResourceSpecification(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#resourceSpecification.
  def exitResourceSpecification(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#resources.
  def enterResources(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#resources.
  def exitResources(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#resource.
  def enterResource(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#resource.
  def exitResource(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#switchBlockStatementGroup.
  def enterSwitchBlockStatementGroup(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#switchBlockStatementGroup.
  def exitSwitchBlockStatementGroup(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#switchLabel.
  def enterSwitchLabel(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#switchLabel.
  def exitSwitchLabel(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#forControl.
  def enterForControl(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#forControl.
  def exitForControl(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#forInit.
  def enterForInit(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#forInit.
  def exitForInit(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#enhancedForControl.
  def enterEnhancedForControl(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#enhancedForControl.
  def exitEnhancedForControl(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#parExpression.
  def enterParExpression(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#parExpression.
  def exitParExpression(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#expressionList.
  def enterExpressionList(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#expressionList.
  def exitExpressionList(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#expression.
  def enterExpression(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#expression.
  def exitExpression(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#lambdaExpression.
  def enterLambdaExpression(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#lambdaExpression.
  def exitLambdaExpression(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#lambdaParameters.
  def enterLambdaParameters(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#lambdaParameters.
  def exitLambdaParameters(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#lambdaBody.
  def enterLambdaBody(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#lambdaBody.
  def exitLambdaBody(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#primary.
  def enterPrimary(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#primary.
  def exitPrimary(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#classType.
  def enterClassType(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#classType.
  def exitClassType(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#creator.
  def enterCreator(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#creator.
  def exitCreator(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#createdName.
  def enterCreatedName(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#createdName.
  def exitCreatedName(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#innerCreator.
  def enterInnerCreator(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#innerCreator.
  def exitInnerCreator(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#arrayCreatorRest.
  def enterArrayCreatorRest(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#arrayCreatorRest.
  def exitArrayCreatorRest(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#classCreatorRest.
  def enterClassCreatorRest(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#classCreatorRest.
  def exitClassCreatorRest(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#explicitGenericInvocation.
  def enterExplicitGenericInvocation(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#explicitGenericInvocation.
  def exitExplicitGenericInvocation(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#typeArgumentsOrDiamond.
  def enterTypeArgumentsOrDiamond(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#typeArgumentsOrDiamond.
  def exitTypeArgumentsOrDiamond(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#nonWildcardTypeArgumentsOrDiamond.
  def enterNonWildcardTypeArgumentsOrDiamond(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#nonWildcardTypeArgumentsOrDiamond.
  def exitNonWildcardTypeArgumentsOrDiamond(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#nonWildcardTypeArguments.
  def enterNonWildcardTypeArguments(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#nonWildcardTypeArguments.
  def exitNonWildcardTypeArguments(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#typeList.
  def enterTypeList(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#typeList.
  def exitTypeList(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#typeType.
  def enterTypeType(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#typeType.
  def exitTypeType(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#primitiveType.
  def enterPrimitiveType(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#primitiveType.
  def exitPrimitiveType(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#typeArguments.
  def enterTypeArguments(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#typeArguments.
  def exitTypeArguments(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#superSuffix.
  def enterSuperSuffix(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#superSuffix.
  def exitSuperSuffix(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#explicitGenericInvocationSuffix.
  def enterExplicitGenericInvocationSuffix(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#explicitGenericInvocationSuffix.
  def exitExplicitGenericInvocationSuffix(self, ctx):
    pass


  # Enter a parse tree produced by JavaParser#arguments.
  def enterArguments(self, ctx):
    pass

  # Exit a parse tree produced by JavaParser#arguments.
  def exitArguments(self, ctx):
    pass


