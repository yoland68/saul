# Generated from Python2.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


from Python2Parser import Python2Parser
from antlr4.Token  import CommonToken

class IndentStack:
    def __init__(self)    : self._s = []
    def empty(self)       : return len(self._s) == 0
    def push(self, wsval) : self._s.append(wsval)
    def pop(self)         : self._s.pop()
    def wsval(self)       : return self._s[-1] if len(self._s) > 0 else 0

class TokenQueue:
    def __init__(self)  : self._q = []
    def empty(self)     : return len(self._q) == 0
    def enq(self, t)    : self._q.append(t)
    def deq(self)       : return self._q.pop(0)


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"T\u02b3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA")
        buf.write(u"\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\t")
        buf.write(u"J\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S")
        buf.write(u"\tS\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write(u"\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write(u"\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write(u"\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write(u"\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write(u"\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3")
        buf.write(u"\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write(u"\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3")
        buf.write(u"\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write(u"\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3")
        buf.write(u"\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3")
        buf.write(u"\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3&")
        buf.write(u"\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3")
        buf.write(u")\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,")
        buf.write(u"\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u"/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62")
        buf.write(u"\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3")
        buf.write(u"\66\3\66\3\67\3\67\3\67\38\38\38\39\39\39\3:\3:\3;\3")
        buf.write(u";\3<\3<\3=\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3B\3C")
        buf.write(u"\3C\3D\3D\3E\3E\3E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3G\3G\7")
        buf.write(u"G\u01af\nG\fG\16G\u01b2\13G\3H\3H\3H\6H\u01b7\nH\rH\16")
        buf.write(u"H\u01b8\3H\3H\3H\5H\u01be\nH\3H\6H\u01c1\nH\rH\16H\u01c2")
        buf.write(u"\5H\u01c5\nH\3H\3H\6H\u01c9\nH\rH\16H\u01ca\3H\5H\u01ce")
        buf.write(u"\nH\3H\3H\6H\u01d2\nH\rH\16H\u01d3\3H\5H\u01d7\nH\5H")
        buf.write(u"\u01d9\nH\3H\6H\u01dc\nH\rH\16H\u01dd\3H\3H\7H\u01e2")
        buf.write(u"\nH\fH\16H\u01e5\13H\3H\3H\6H\u01e9\nH\rH\16H\u01ea\5")
        buf.write(u"H\u01ed\nH\3H\3H\5H\u01f1\nH\3H\6H\u01f4\nH\rH\16H\u01f5")
        buf.write(u"\5H\u01f8\nH\3H\5H\u01fb\nH\3H\6H\u01fe\nH\rH\16H\u01ff")
        buf.write(u"\3H\3H\3H\5H\u0205\nH\3H\6H\u0208\nH\rH\16H\u0209\3H")
        buf.write(u"\5H\u020d\nH\3H\5H\u0210\nH\5H\u0212\nH\3I\5I\u0215\n")
        buf.write(u"I\3I\5I\u0218\nI\3I\5I\u021b\nI\3I\5I\u021e\nI\5I\u0220")
        buf.write(u"\nI\3I\3I\3I\6I\u0225\nI\rI\16I\u0226\3I\5I\u022a\nI")
        buf.write(u"\3I\5I\u022d\nI\3I\5I\u0230\nI\3I\7I\u0233\nI\fI\16I")
        buf.write(u"\u0236\13I\3I\3I\3I\3I\6I\u023c\nI\rI\16I\u023d\3I\5")
        buf.write(u"I\u0241\nI\3I\5I\u0244\nI\3I\5I\u0247\nI\3I\7I\u024a")
        buf.write(u"\nI\fI\16I\u024d\13I\3I\3I\3I\3I\3I\3I\3I\3I\7I\u0257")
        buf.write(u"\nI\fI\16I\u025a\13I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\7")
        buf.write(u"I\u0266\nI\fI\16I\u0269\13I\3I\3I\3I\5I\u026e\nI\3J\5")
        buf.write(u"J\u0271\nJ\3J\6J\u0274\nJ\rJ\16J\u0275\3J\3J\3J\7J\u027b")
        buf.write(u"\nJ\fJ\16J\u027e\13J\3J\5J\u0281\nJ\3J\3J\3J\5J\u0286")
        buf.write(u"\nJ\3J\3J\3J\3J\3K\6K\u028d\nK\rK\16K\u028e\3K\3K\3K")
        buf.write(u"\3K\3L\3L\7L\u0297\nL\fL\16L\u029a\13L\3L\3L\3M\3M\3")
        buf.write(u"M\3N\3N\3N\3O\3O\3O\3P\3P\3P\3Q\3Q\3Q\3R\3R\3R\3S\3S")
        buf.write(u"\3S\3S\4\u0258\u0267\2T\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write(u"\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write(u"%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(u";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write(u"e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083")
        buf.write(u"C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093")
        buf.write(u"K\u0095L\u0097M\u0099N\u009bO\u009dP\u009fQ\u00a1R\u00a3")
        buf.write(u"S\u00a5T\3\2\26\5\2C\\aac|\6\2\62;C\\aac|\4\2ZZzz\5\2")
        buf.write(u"\62;CHch\4\2NNnn\4\2GGgg\4\2--//\3\2\62;\4\2QQqq\3\2")
        buf.write(u"\629\4\2DDdd\3\2\62\63\4\2LLll\6\2DDWWddww\4\2TTtt\4")
        buf.write(u"\2\13\13\"\"\6\2\f\f\17\17))^^\6\2\f\f\17\17$$^^\3\2")
        buf.write(u"^^\4\2\f\f\17\17\2\u02ee\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write(u"\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write(u"\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write(u"\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write(u"\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(u")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write(u"\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write(u"\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write(u"\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write(u"\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write(u"\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write(u"a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write(u"\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write(u"\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2")
        buf.write(u"\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write(u"\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write(u"\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2")
        buf.write(u"\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2")
        buf.write(u"\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write(u"\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2")
        buf.write(u"\2\2\3\u00a7\3\2\2\2\5\u00a9\3\2\2\2\7\u00ad\3\2\2\2")
        buf.write(u"\t\u00af\3\2\2\2\13\u00b1\3\2\2\2\r\u00b3\3\2\2\2\17")
        buf.write(u"\u00b5\3\2\2\2\21\u00b8\3\2\2\2\23\u00ba\3\2\2\2\25\u00bd")
        buf.write(u"\3\2\2\2\27\u00c0\3\2\2\2\31\u00c3\3\2\2\2\33\u00c6\3")
        buf.write(u"\2\2\2\35\u00c9\3\2\2\2\37\u00cc\3\2\2\2!\u00cf\3\2\2")
        buf.write(u"\2#\u00d2\3\2\2\2%\u00d6\3\2\2\2\'\u00da\3\2\2\2)\u00de")
        buf.write(u"\3\2\2\2+\u00e2\3\2\2\2-\u00e5\3\2\2\2/\u00e9\3\2\2\2")
        buf.write(u"\61\u00ee\3\2\2\2\63\u00f4\3\2\2\2\65\u00fd\3\2\2\2\67")
        buf.write(u"\u0104\3\2\2\29\u010a\3\2\2\2;\u0111\3\2\2\2=\u0116\3")
        buf.write(u"\2\2\2?\u0118\3\2\2\2A\u011b\3\2\2\2C\u0122\3\2\2\2E")
        buf.write(u"\u0127\3\2\2\2G\u012a\3\2\2\2I\u0131\3\2\2\2K\u0134\3")
        buf.write(u"\2\2\2M\u0139\3\2\2\2O\u013e\3\2\2\2Q\u0144\3\2\2\2S")
        buf.write(u"\u0148\3\2\2\2U\u014c\3\2\2\2W\u0154\3\2\2\2Y\u0159\3")
        buf.write(u"\2\2\2[\u0160\3\2\2\2]\u0167\3\2\2\2_\u016a\3\2\2\2a")
        buf.write(u"\u016e\3\2\2\2c\u0172\3\2\2\2e\u0174\3\2\2\2g\u0176\3")
        buf.write(u"\2\2\2i\u0179\3\2\2\2k\u017c\3\2\2\2m\u017f\3\2\2\2o")
        buf.write(u"\u0182\3\2\2\2q\u0185\3\2\2\2s\u0188\3\2\2\2u\u018a\3")
        buf.write(u"\2\2\2w\u018c\3\2\2\2y\u018e\3\2\2\2{\u0191\3\2\2\2}")
        buf.write(u"\u0193\3\2\2\2\177\u0195\3\2\2\2\u0081\u0197\3\2\2\2")
        buf.write(u"\u0083\u0199\3\2\2\2\u0085\u019c\3\2\2\2\u0087\u019e")
        buf.write(u"\3\2\2\2\u0089\u01a0\3\2\2\2\u008b\u01a6\3\2\2\2\u008d")
        buf.write(u"\u01ac\3\2\2\2\u008f\u0211\3\2\2\2\u0091\u021f\3\2\2")
        buf.write(u"\2\u0093\u0285\3\2\2\2\u0095\u028c\3\2\2\2\u0097\u0294")
        buf.write(u"\3\2\2\2\u0099\u029d\3\2\2\2\u009b\u02a0\3\2\2\2\u009d")
        buf.write(u"\u02a3\3\2\2\2\u009f\u02a6\3\2\2\2\u00a1\u02a9\3\2\2")
        buf.write(u"\2\u00a3\u02ac\3\2\2\2\u00a5\u02af\3\2\2\2\u00a7\u00a8")
        buf.write(u"\7B\2\2\u00a8\4\3\2\2\2\u00a9\u00aa\7f\2\2\u00aa\u00ab")
        buf.write(u"\7g\2\2\u00ab\u00ac\7h\2\2\u00ac\6\3\2\2\2\u00ad\u00ae")
        buf.write(u"\7<\2\2\u00ae\b\3\2\2\2\u00af\u00b0\7?\2\2\u00b0\n\3")
        buf.write(u"\2\2\2\u00b1\u00b2\7.\2\2\u00b2\f\3\2\2\2\u00b3\u00b4")
        buf.write(u"\7,\2\2\u00b4\16\3\2\2\2\u00b5\u00b6\7,\2\2\u00b6\u00b7")
        buf.write(u"\7,\2\2\u00b7\20\3\2\2\2\u00b8\u00b9\7=\2\2\u00b9\22")
        buf.write(u"\3\2\2\2\u00ba\u00bb\7-\2\2\u00bb\u00bc\7?\2\2\u00bc")
        buf.write(u"\24\3\2\2\2\u00bd\u00be\7/\2\2\u00be\u00bf\7?\2\2\u00bf")
        buf.write(u"\26\3\2\2\2\u00c0\u00c1\7,\2\2\u00c1\u00c2\7?\2\2\u00c2")
        buf.write(u"\30\3\2\2\2\u00c3\u00c4\7\61\2\2\u00c4\u00c5\7?\2\2\u00c5")
        buf.write(u"\32\3\2\2\2\u00c6\u00c7\7\'\2\2\u00c7\u00c8\7?\2\2\u00c8")
        buf.write(u"\34\3\2\2\2\u00c9\u00ca\7(\2\2\u00ca\u00cb\7?\2\2\u00cb")
        buf.write(u"\36\3\2\2\2\u00cc\u00cd\7~\2\2\u00cd\u00ce\7?\2\2\u00ce")
        buf.write(u" \3\2\2\2\u00cf\u00d0\7`\2\2\u00d0\u00d1\7?\2\2\u00d1")
        buf.write(u"\"\3\2\2\2\u00d2\u00d3\7>\2\2\u00d3\u00d4\7>\2\2\u00d4")
        buf.write(u"\u00d5\7?\2\2\u00d5$\3\2\2\2\u00d6\u00d7\7@\2\2\u00d7")
        buf.write(u"\u00d8\7@\2\2\u00d8\u00d9\7?\2\2\u00d9&\3\2\2\2\u00da")
        buf.write(u"\u00db\7,\2\2\u00db\u00dc\7,\2\2\u00dc\u00dd\7?\2\2\u00dd")
        buf.write(u"(\3\2\2\2\u00de\u00df\7\61\2\2\u00df\u00e0\7\61\2\2\u00e0")
        buf.write(u"\u00e1\7?\2\2\u00e1*\3\2\2\2\u00e2\u00e3\7@\2\2\u00e3")
        buf.write(u"\u00e4\7@\2\2\u00e4,\3\2\2\2\u00e5\u00e6\7f\2\2\u00e6")
        buf.write(u"\u00e7\7g\2\2\u00e7\u00e8\7n\2\2\u00e8.\3\2\2\2\u00e9")
        buf.write(u"\u00ea\7r\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7u\2\2\u00ec")
        buf.write(u"\u00ed\7u\2\2\u00ed\60\3\2\2\2\u00ee\u00ef\7d\2\2\u00ef")
        buf.write(u"\u00f0\7t\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2\7c\2\2\u00f2")
        buf.write(u"\u00f3\7m\2\2\u00f3\62\3\2\2\2\u00f4\u00f5\7e\2\2\u00f5")
        buf.write(u"\u00f6\7q\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7v\2\2\u00f8")
        buf.write(u"\u00f9\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7w\2\2\u00fb")
        buf.write(u"\u00fc\7g\2\2\u00fc\64\3\2\2\2\u00fd\u00fe\7t\2\2\u00fe")
        buf.write(u"\u00ff\7g\2\2\u00ff\u0100\7v\2\2\u0100\u0101\7w\2\2\u0101")
        buf.write(u"\u0102\7t\2\2\u0102\u0103\7p\2\2\u0103\66\3\2\2\2\u0104")
        buf.write(u"\u0105\7t\2\2\u0105\u0106\7c\2\2\u0106\u0107\7k\2\2\u0107")
        buf.write(u"\u0108\7u\2\2\u0108\u0109\7g\2\2\u01098\3\2\2\2\u010a")
        buf.write(u"\u010b\7k\2\2\u010b\u010c\7o\2\2\u010c\u010d\7r\2\2\u010d")
        buf.write(u"\u010e\7q\2\2\u010e\u010f\7t\2\2\u010f\u0110\7v\2\2\u0110")
        buf.write(u":\3\2\2\2\u0111\u0112\7h\2\2\u0112\u0113\7t\2\2\u0113")
        buf.write(u"\u0114\7q\2\2\u0114\u0115\7o\2\2\u0115<\3\2\2\2\u0116")
        buf.write(u"\u0117\7\60\2\2\u0117>\3\2\2\2\u0118\u0119\7c\2\2\u0119")
        buf.write(u"\u011a\7u\2\2\u011a@\3\2\2\2\u011b\u011c\7i\2\2\u011c")
        buf.write(u"\u011d\7n\2\2\u011d\u011e\7q\2\2\u011e\u011f\7d\2\2\u011f")
        buf.write(u"\u0120\7c\2\2\u0120\u0121\7n\2\2\u0121B\3\2\2\2\u0122")
        buf.write(u"\u0123\7g\2\2\u0123\u0124\7z\2\2\u0124\u0125\7g\2\2\u0125")
        buf.write(u"\u0126\7e\2\2\u0126D\3\2\2\2\u0127\u0128\7k\2\2\u0128")
        buf.write(u"\u0129\7p\2\2\u0129F\3\2\2\2\u012a\u012b\7c\2\2\u012b")
        buf.write(u"\u012c\7u\2\2\u012c\u012d\7u\2\2\u012d\u012e\7g\2\2\u012e")
        buf.write(u"\u012f\7t\2\2\u012f\u0130\7v\2\2\u0130H\3\2\2\2\u0131")
        buf.write(u"\u0132\7k\2\2\u0132\u0133\7h\2\2\u0133J\3\2\2\2\u0134")
        buf.write(u"\u0135\7g\2\2\u0135\u0136\7n\2\2\u0136\u0137\7k\2\2\u0137")
        buf.write(u"\u0138\7h\2\2\u0138L\3\2\2\2\u0139\u013a\7g\2\2\u013a")
        buf.write(u"\u013b\7n\2\2\u013b\u013c\7u\2\2\u013c\u013d\7g\2\2\u013d")
        buf.write(u"N\3\2\2\2\u013e\u013f\7y\2\2\u013f\u0140\7j\2\2\u0140")
        buf.write(u"\u0141\7k\2\2\u0141\u0142\7n\2\2\u0142\u0143\7g\2\2\u0143")
        buf.write(u"P\3\2\2\2\u0144\u0145\7h\2\2\u0145\u0146\7q\2\2\u0146")
        buf.write(u"\u0147\7t\2\2\u0147R\3\2\2\2\u0148\u0149\7v\2\2\u0149")
        buf.write(u"\u014a\7t\2\2\u014a\u014b\7{\2\2\u014bT\3\2\2\2\u014c")
        buf.write(u"\u014d\7h\2\2\u014d\u014e\7k\2\2\u014e\u014f\7p\2\2\u014f")
        buf.write(u"\u0150\7c\2\2\u0150\u0151\7n\2\2\u0151\u0152\7n\2\2\u0152")
        buf.write(u"\u0153\7{\2\2\u0153V\3\2\2\2\u0154\u0155\7y\2\2\u0155")
        buf.write(u"\u0156\7k\2\2\u0156\u0157\7v\2\2\u0157\u0158\7j\2\2\u0158")
        buf.write(u"X\3\2\2\2\u0159\u015a\7g\2\2\u015a\u015b\7z\2\2\u015b")
        buf.write(u"\u015c\7e\2\2\u015c\u015d\7g\2\2\u015d\u015e\7r\2\2\u015e")
        buf.write(u"\u015f\7v\2\2\u015fZ\3\2\2\2\u0160\u0161\7n\2\2\u0161")
        buf.write(u"\u0162\7c\2\2\u0162\u0163\7o\2\2\u0163\u0164\7d\2\2\u0164")
        buf.write(u"\u0165\7f\2\2\u0165\u0166\7c\2\2\u0166\\\3\2\2\2\u0167")
        buf.write(u"\u0168\7q\2\2\u0168\u0169\7t\2\2\u0169^\3\2\2\2\u016a")
        buf.write(u"\u016b\7c\2\2\u016b\u016c\7p\2\2\u016c\u016d\7f\2\2\u016d")
        buf.write(u"`\3\2\2\2\u016e\u016f\7p\2\2\u016f\u0170\7q\2\2\u0170")
        buf.write(u"\u0171\7v\2\2\u0171b\3\2\2\2\u0172\u0173\7>\2\2\u0173")
        buf.write(u"d\3\2\2\2\u0174\u0175\7@\2\2\u0175f\3\2\2\2\u0176\u0177")
        buf.write(u"\7?\2\2\u0177\u0178\7?\2\2\u0178h\3\2\2\2\u0179\u017a")
        buf.write(u"\7@\2\2\u017a\u017b\7?\2\2\u017bj\3\2\2\2\u017c\u017d")
        buf.write(u"\7>\2\2\u017d\u017e\7?\2\2\u017el\3\2\2\2\u017f\u0180")
        buf.write(u"\7>\2\2\u0180\u0181\7@\2\2\u0181n\3\2\2\2\u0182\u0183")
        buf.write(u"\7#\2\2\u0183\u0184\7?\2\2\u0184p\3\2\2\2\u0185\u0186")
        buf.write(u"\7k\2\2\u0186\u0187\7u\2\2\u0187r\3\2\2\2\u0188\u0189")
        buf.write(u"\7~\2\2\u0189t\3\2\2\2\u018a\u018b\7`\2\2\u018bv\3\2")
        buf.write(u"\2\2\u018c\u018d\7(\2\2\u018dx\3\2\2\2\u018e\u018f\7")
        buf.write(u">\2\2\u018f\u0190\7>\2\2\u0190z\3\2\2\2\u0191\u0192\7")
        buf.write(u"-\2\2\u0192|\3\2\2\2\u0193\u0194\7/\2\2\u0194~\3\2\2")
        buf.write(u"\2\u0195\u0196\7\61\2\2\u0196\u0080\3\2\2\2\u0197\u0198")
        buf.write(u"\7\'\2\2\u0198\u0082\3\2\2\2\u0199\u019a\7\61\2\2\u019a")
        buf.write(u"\u019b\7\61\2\2\u019b\u0084\3\2\2\2\u019c\u019d\7\u0080")
        buf.write(u"\2\2\u019d\u0086\3\2\2\2\u019e\u019f\7b\2\2\u019f\u0088")
        buf.write(u"\3\2\2\2\u01a0\u01a1\7e\2\2\u01a1\u01a2\7n\2\2\u01a2")
        buf.write(u"\u01a3\7c\2\2\u01a3\u01a4\7u\2\2\u01a4\u01a5\7u\2\2\u01a5")
        buf.write(u"\u008a\3\2\2\2\u01a6\u01a7\7{\2\2\u01a7\u01a8\7k\2\2")
        buf.write(u"\u01a8\u01a9\7g\2\2\u01a9\u01aa\7n\2\2\u01aa\u01ab\7")
        buf.write(u"f\2\2\u01ab\u008c\3\2\2\2\u01ac\u01b0\t\2\2\2\u01ad\u01af")
        buf.write(u"\t\3\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0")
        buf.write(u"\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u008e\3\2\2")
        buf.write(u"\2\u01b2\u01b0\3\2\2\2\u01b3\u01d8\7\62\2\2\u01b4\u01b6")
        buf.write(u"\t\4\2\2\u01b5\u01b7\t\5\2\2\u01b6\u01b5\3\2\2\2\u01b7")
        buf.write(u"\u01b8\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2")
        buf.write(u"\2\u01b9\u01c4\3\2\2\2\u01ba\u01c5\t\6\2\2\u01bb\u01bd")
        buf.write(u"\t\7\2\2\u01bc\u01be\t\b\2\2\u01bd\u01bc\3\2\2\2\u01bd")
        buf.write(u"\u01be\3\2\2\2\u01be\u01c0\3\2\2\2\u01bf\u01c1\t\t\2")
        buf.write(u"\2\u01c0\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c0")
        buf.write(u"\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c5\3\2\2\2\u01c4")
        buf.write(u"\u01ba\3\2\2\2\u01c4\u01bb\3\2\2\2\u01c4\u01c5\3\2\2")
        buf.write(u"\2\u01c5\u01d9\3\2\2\2\u01c6\u01c8\t\n\2\2\u01c7\u01c9")
        buf.write(u"\t\13\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write(u"\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cd\3\2\2")
        buf.write(u"\2\u01cc\u01ce\t\6\2\2\u01cd\u01cc\3\2\2\2\u01cd\u01ce")
        buf.write(u"\3\2\2\2\u01ce\u01d9\3\2\2\2\u01cf\u01d1\t\f\2\2\u01d0")
        buf.write(u"\u01d2\t\r\2\2\u01d1\u01d0\3\2\2\2\u01d2\u01d3\3\2\2")
        buf.write(u"\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d6")
        buf.write(u"\3\2\2\2\u01d5\u01d7\t\6\2\2\u01d6\u01d5\3\2\2\2\u01d6")
        buf.write(u"\u01d7\3\2\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01b4\3\2\2")
        buf.write(u"\2\u01d8\u01c6\3\2\2\2\u01d8\u01cf\3\2\2\2\u01d9\u0212")
        buf.write(u"\3\2\2\2\u01da\u01dc\t\t\2\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write(u"\u01dd\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2")
        buf.write(u"\2\u01de\u01df\3\2\2\2\u01df\u01e3\7\60\2\2\u01e0\u01e2")
        buf.write(u"\t\t\2\2\u01e1\u01e0\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3")
        buf.write(u"\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01ed\3\2\2")
        buf.write(u"\2\u01e5\u01e3\3\2\2\2\u01e6\u01e8\7\60\2\2\u01e7\u01e9")
        buf.write(u"\t\t\2\2\u01e8\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea")
        buf.write(u"\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ed\3\2\2")
        buf.write(u"\2\u01ec\u01db\3\2\2\2\u01ec\u01e6\3\2\2\2\u01ed\u01f7")
        buf.write(u"\3\2\2\2\u01ee\u01f0\t\7\2\2\u01ef\u01f1\t\b\2\2\u01f0")
        buf.write(u"\u01ef\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f3\3\2\2")
        buf.write(u"\2\u01f2\u01f4\t\t\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f5")
        buf.write(u"\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write(u"\u01f8\3\2\2\2\u01f7\u01ee\3\2\2\2\u01f7\u01f8\3\2\2")
        buf.write(u"\2\u01f8\u01fa\3\2\2\2\u01f9\u01fb\t\16\2\2\u01fa\u01f9")
        buf.write(u"\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u0212\3\2\2\2\u01fc")
        buf.write(u"\u01fe\t\t\2\2\u01fd\u01fc\3\2\2\2\u01fe\u01ff\3\2\2")
        buf.write(u"\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u020f")
        buf.write(u"\3\2\2\2\u0201\u0210\t\6\2\2\u0202\u0204\t\7\2\2\u0203")
        buf.write(u"\u0205\t\b\2\2\u0204\u0203\3\2\2\2\u0204\u0205\3\2\2")
        buf.write(u"\2\u0205\u0207\3\2\2\2\u0206\u0208\t\t\2\2\u0207\u0206")
        buf.write(u"\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u0207\3\2\2\2\u0209")
        buf.write(u"\u020a\3\2\2\2\u020a\u020c\3\2\2\2\u020b\u020d\t\16\2")
        buf.write(u"\2\u020c\u020b\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u0210")
        buf.write(u"\3\2\2\2\u020e\u0210\t\16\2\2\u020f\u0201\3\2\2\2\u020f")
        buf.write(u"\u0202\3\2\2\2\u020f\u020e\3\2\2\2\u020f\u0210\3\2\2")
        buf.write(u"\2\u0210\u0212\3\2\2\2\u0211\u01b3\3\2\2\2\u0211\u01ec")
        buf.write(u"\3\2\2\2\u0211\u01fd\3\2\2\2\u0212\u0090\3\2\2\2\u0213")
        buf.write(u"\u0215\t\17\2\2\u0214\u0213\3\2\2\2\u0214\u0215\3\2\2")
        buf.write(u"\2\u0215\u0217\3\2\2\2\u0216\u0218\t\20\2\2\u0217\u0216")
        buf.write(u"\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0220\3\2\2\2\u0219")
        buf.write(u"\u021b\t\20\2\2\u021a\u0219\3\2\2\2\u021a\u021b\3\2\2")
        buf.write(u"\2\u021b\u021d\3\2\2\2\u021c\u021e\t\17\2\2\u021d\u021c")
        buf.write(u"\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u0220\3\2\2\2\u021f")
        buf.write(u"\u0214\3\2\2\2\u021f\u021a\3\2\2\2\u0220\u026d\3\2\2")
        buf.write(u"\2\u0221\u0234\7)\2\2\u0222\u022f\7^\2\2\u0223\u0225")
        buf.write(u"\t\21\2\2\u0224\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226")
        buf.write(u"\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u022c\3\2\2")
        buf.write(u"\2\u0228\u022a\7\17\2\2\u0229\u0228\3\2\2\2\u0229\u022a")
        buf.write(u"\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022d\7\f\2\2\u022c")
        buf.write(u"\u0229\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u0230\3\2\2")
        buf.write(u"\2\u022e\u0230\13\2\2\2\u022f\u0224\3\2\2\2\u022f\u022e")
        buf.write(u"\3\2\2\2\u0230\u0233\3\2\2\2\u0231\u0233\n\22\2\2\u0232")
        buf.write(u"\u0222\3\2\2\2\u0232\u0231\3\2\2\2\u0233\u0236\3\2\2")
        buf.write(u"\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0237")
        buf.write(u"\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u026e\7)\2\2\u0238")
        buf.write(u"\u024b\7$\2\2\u0239\u0246\7^\2\2\u023a\u023c\t\21\2\2")
        buf.write(u"\u023b\u023a\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023b")
        buf.write(u"\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u0243\3\2\2\2\u023f")
        buf.write(u"\u0241\7\17\2\2\u0240\u023f\3\2\2\2\u0240\u0241\3\2\2")
        buf.write(u"\2\u0241\u0242\3\2\2\2\u0242\u0244\7\f\2\2\u0243\u0240")
        buf.write(u"\3\2\2\2\u0243\u0244\3\2\2\2\u0244\u0247\3\2\2\2\u0245")
        buf.write(u"\u0247\13\2\2\2\u0246\u023b\3\2\2\2\u0246\u0245\3\2\2")
        buf.write(u"\2\u0247\u024a\3\2\2\2\u0248\u024a\n\23\2\2\u0249\u0239")
        buf.write(u"\3\2\2\2\u0249\u0248\3\2\2\2\u024a\u024d\3\2\2\2\u024b")
        buf.write(u"\u0249\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024e\3\2\2")
        buf.write(u"\2\u024d\u024b\3\2\2\2\u024e\u026e\7$\2\2\u024f\u0250")
        buf.write(u"\7$\2\2\u0250\u0251\7$\2\2\u0251\u0252\7$\2\2\u0252\u0258")
        buf.write(u"\3\2\2\2\u0253\u0254\7^\2\2\u0254\u0257\13\2\2\2\u0255")
        buf.write(u"\u0257\n\24\2\2\u0256\u0253\3\2\2\2\u0256\u0255\3\2\2")
        buf.write(u"\2\u0257\u025a\3\2\2\2\u0258\u0259\3\2\2\2\u0258\u0256")
        buf.write(u"\3\2\2\2\u0259\u025b\3\2\2\2\u025a\u0258\3\2\2\2\u025b")
        buf.write(u"\u025c\7$\2\2\u025c\u025d\7$\2\2\u025d\u026e\7$\2\2\u025e")
        buf.write(u"\u025f\7)\2\2\u025f\u0260\7)\2\2\u0260\u0261\7)\2\2\u0261")
        buf.write(u"\u0267\3\2\2\2\u0262\u0263\7^\2\2\u0263\u0266\13\2\2")
        buf.write(u"\2\u0264\u0266\n\24\2\2\u0265\u0262\3\2\2\2\u0265\u0264")
        buf.write(u"\3\2\2\2\u0266\u0269\3\2\2\2\u0267\u0268\3\2\2\2\u0267")
        buf.write(u"\u0265\3\2\2\2\u0268\u026a\3\2\2\2\u0269\u0267\3\2\2")
        buf.write(u"\2\u026a\u026b\7)\2\2\u026b\u026c\7)\2\2\u026c\u026e")
        buf.write(u"\7)\2\2\u026d\u0221\3\2\2\2\u026d\u0238\3\2\2\2\u026d")
        buf.write(u"\u024f\3\2\2\2\u026d\u025e\3\2\2\2\u026e\u0092\3\2\2")
        buf.write(u"\2\u026f\u0271\7\17\2\2\u0270\u026f\3\2\2\2\u0270\u0271")
        buf.write(u"\3\2\2\2\u0271\u0272\3\2\2\2\u0272\u0274\7\f\2\2\u0273")
        buf.write(u"\u0270\3\2\2\2\u0274\u0275\3\2\2\2\u0275\u0273\3\2\2")
        buf.write(u"\2\u0275\u0276\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u0286")
        buf.write(u"\bJ\2\2\u0278\u027c\7^\2\2\u0279\u027b\t\21\2\2\u027a")
        buf.write(u"\u0279\3\2\2\2\u027b\u027e\3\2\2\2\u027c\u027a\3\2\2")
        buf.write(u"\2\u027c\u027d\3\2\2\2\u027d\u0280\3\2\2\2\u027e\u027c")
        buf.write(u"\3\2\2\2\u027f\u0281\7\17\2\2\u0280\u027f\3\2\2\2\u0280")
        buf.write(u"\u0281\3\2\2\2\u0281\u0282\3\2\2\2\u0282\u0283\7\f\2")
        buf.write(u"\2\u0283\u0284\3\2\2\2\u0284\u0286\bJ\3\2\u0285\u0273")
        buf.write(u"\3\2\2\2\u0285\u0278\3\2\2\2\u0286\u0287\3\2\2\2\u0287")
        buf.write(u"\u0288\bJ\4\2\u0288\u0289\3\2\2\2\u0289\u028a\bJ\5\2")
        buf.write(u"\u028a\u0094\3\2\2\2\u028b\u028d\t\21\2\2\u028c\u028b")
        buf.write(u"\3\2\2\2\u028d\u028e\3\2\2\2\u028e\u028c\3\2\2\2\u028e")
        buf.write(u"\u028f\3\2\2\2\u028f\u0290\3\2\2\2\u0290\u0291\bK\6\2")
        buf.write(u"\u0291\u0292\3\2\2\2\u0292\u0293\bK\5\2\u0293\u0096\3")
        buf.write(u"\2\2\2\u0294\u0298\7%\2\2\u0295\u0297\n\25\2\2\u0296")
        buf.write(u"\u0295\3\2\2\2\u0297\u029a\3\2\2\2\u0298\u0296\3\2\2")
        buf.write(u"\2\u0298\u0299\3\2\2\2\u0299\u029b\3\2\2\2\u029a\u0298")
        buf.write(u"\3\2\2\2\u029b\u029c\bL\7\2\u029c\u0098\3\2\2\2\u029d")
        buf.write(u"\u029e\7*\2\2\u029e\u029f\bM\b\2\u029f\u009a\3\2\2\2")
        buf.write(u"\u02a0\u02a1\7+\2\2\u02a1\u02a2\bN\t\2\u02a2\u009c\3")
        buf.write(u"\2\2\2\u02a3\u02a4\7}\2\2\u02a4\u02a5\bO\n\2\u02a5\u009e")
        buf.write(u"\3\2\2\2\u02a6\u02a7\7\177\2\2\u02a7\u02a8\bP\13\2\u02a8")
        buf.write(u"\u00a0\3\2\2\2\u02a9\u02aa\7]\2\2\u02aa\u02ab\bQ\f\2")
        buf.write(u"\u02ab\u00a2\3\2\2\2\u02ac\u02ad\7_\2\2\u02ad\u02ae\b")
        buf.write(u"R\r\2\u02ae\u00a4\3\2\2\2\u02af\u02b0\13\2\2\2\u02b0")
        buf.write(u"\u02b1\3\2\2\2\u02b1\u02b2\bS\7\2\u02b2\u00a6\3\2\2\2")
        buf.write(u"8\2\u01b0\u01b8\u01bd\u01c2\u01c4\u01ca\u01cd\u01d3\u01d6")
        buf.write(u"\u01d8\u01dd\u01e3\u01ea\u01ec\u01f0\u01f5\u01f7\u01fa")
        buf.write(u"\u01ff\u0204\u0209\u020c\u020f\u0211\u0214\u0217\u021a")
        buf.write(u"\u021d\u021f\u0226\u0229\u022c\u022f\u0232\u0234\u023d")
        buf.write(u"\u0240\u0243\u0246\u0249\u024b\u0256\u0258\u0265\u0267")
        buf.write(u"\u026d\u0270\u0275\u027c\u0280\u0285\u028e\u0298\16\3")
        buf.write(u"J\2\3J\3\3J\4\2\3\2\3K\5\b\2\2\3M\6\3N\7\3O\b\3P\t\3")
        buf.write(u"Q\n\3R\13")
        return buf.getvalue()


class Python2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    T__59 = 60
    T__60 = 61
    T__61 = 62
    T__62 = 63
    T__63 = 64
    T__64 = 65
    T__65 = 66
    T__66 = 67
    T__67 = 68
    T__68 = 69
    NAME = 70
    NUMBER = 71
    STRING = 72
    LINENDING = 73
    WHITESPACE = 74
    COMMENT = 75
    OPEN_PAREN = 76
    CLOSE_PAREN = 77
    OPEN_BRACE = 78
    CLOSE_BRACE = 79
    OPEN_BRACKET = 80
    CLOSE_BRACKET = 81
    UNKNOWN = 82

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'@'", u"'def'", u"':'", u"'='", u"','", u"'*'", u"'**'", u"';'", 
            u"'+='", u"'-='", u"'*='", u"'/='", u"'%='", u"'&='", u"'|='", 
            u"'^='", u"'<<='", u"'>>='", u"'**='", u"'//='", u"'>>'", u"'del'", 
            u"'pass'", u"'break'", u"'continue'", u"'return'", u"'raise'", 
            u"'import'", u"'from'", u"'.'", u"'as'", u"'global'", u"'exec'", 
            u"'in'", u"'assert'", u"'if'", u"'elif'", u"'else'", u"'while'", 
            u"'for'", u"'try'", u"'finally'", u"'with'", u"'except'", u"'lambda'", 
            u"'or'", u"'and'", u"'not'", u"'<'", u"'>'", u"'=='", u"'>='", 
            u"'<='", u"'<>'", u"'!='", u"'is'", u"'|'", u"'^'", u"'&'", 
            u"'<<'", u"'+'", u"'-'", u"'/'", u"'%'", u"'//'", u"'~'", u"'`'", 
            u"'class'", u"'yield'", u"'('", u"')'", u"'{'", u"'}'", u"'['", 
            u"']'" ]

    symbolicNames = [ u"<INVALID>",
            u"NAME", u"NUMBER", u"STRING", u"LINENDING", u"WHITESPACE", 
            u"COMMENT", u"OPEN_PAREN", u"CLOSE_PAREN", u"OPEN_BRACE", u"CLOSE_BRACE", 
            u"OPEN_BRACKET", u"CLOSE_BRACKET", u"UNKNOWN" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"T__9", u"T__10", u"T__11", 
                  u"T__12", u"T__13", u"T__14", u"T__15", u"T__16", u"T__17", 
                  u"T__18", u"T__19", u"T__20", u"T__21", u"T__22", u"T__23", 
                  u"T__24", u"T__25", u"T__26", u"T__27", u"T__28", u"T__29", 
                  u"T__30", u"T__31", u"T__32", u"T__33", u"T__34", u"T__35", 
                  u"T__36", u"T__37", u"T__38", u"T__39", u"T__40", u"T__41", 
                  u"T__42", u"T__43", u"T__44", u"T__45", u"T__46", u"T__47", 
                  u"T__48", u"T__49", u"T__50", u"T__51", u"T__52", u"T__53", 
                  u"T__54", u"T__55", u"T__56", u"T__57", u"T__58", u"T__59", 
                  u"T__60", u"T__61", u"T__62", u"T__63", u"T__64", u"T__65", 
                  u"T__66", u"T__67", u"T__68", u"NAME", u"NUMBER", u"STRING", 
                  u"LINENDING", u"WHITESPACE", u"COMMENT", u"OPEN_PAREN", 
                  u"CLOSE_PAREN", u"OPEN_BRACE", u"CLOSE_BRACE", u"OPEN_BRACKET", 
                  u"CLOSE_BRACKET", u"UNKNOWN" ]

    grammarFileName = u"Python2.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(Python2Lexer, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


        # Indented to append code to the constructor.
        self._openBRCount       = 0
        self._suppressNewlines  = False
        self._lineContinuation  = False
        self._tokens            = TokenQueue()
        self._indents           = IndentStack()

    def nextToken(self):
        if not self._tokens.empty():
            return self._tokens.deq()
        else:
            t = super(Python2Lexer, self).nextToken()
            if t.type != Token.EOF:
                return t
            else:
                if not self._suppressNewlines:
                    self.emitNewline()
                self.emitFullDedent()
                self.emitEndmarker()
                self.emitEndToken(t)
                return self._tokens.deq()
                
    def emitEndToken(self, token):
        self._tokens.enq(token)

    def emitIndent(self, length=0, text='INDENT'):
        t = self.createToken(Python2Parser.INDENT, text, length)
        self._tokens.enq(t)

    def emitDedent(self):
        t = self.createToken(Python2Parser.DEDENT, 'DEDENT')
        self._tokens.enq(t)

    def emitFullDedent(self):
        while not self._indents.empty():
            self._indents.pop()
            self.emitDedent()

    def emitEndmarker(self):
        t = self.createToken(Python2Parser.ENDMARKER, 'ENDMARKER')
        self._tokens.enq(t)

    def emitNewline(self):
        t = self.createToken(Python2Parser.NEWLINE, 'NEWLINE')
        self._tokens.enq(t)

    def createToken(self, type_, text="", length=0):
        start = self._tokenStartCharIndex
        stop = start + length
        t = CommonToken(self._tokenFactorySourcePair,
                        type_, self.DEFAULT_TOKEN_CHANNEL,
                        start, stop)
        t.text = text
        return t


    def action(self, localctx, ruleIndex, actionIndex):
    	if self._actions is None:
    		actions = dict()
    		actions[72] = self.LINENDING_action 
    		actions[73] = self.WHITESPACE_action 
    		actions[75] = self.OPEN_PAREN_action 
    		actions[76] = self.CLOSE_PAREN_action 
    		actions[77] = self.OPEN_BRACE_action 
    		actions[78] = self.CLOSE_BRACE_action 
    		actions[79] = self.OPEN_BRACKET_action 
    		actions[80] = self.CLOSE_BRACKET_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def LINENDING_action(self, localctx , actionIndex):
        if actionIndex == 0:
            self._lineContinuation=False
     

        if actionIndex == 1:
            self._lineContinuation=True
     

        if actionIndex == 2:

            if self._openBRCount == 0 and not self._lineContinuation:
                if not self._suppressNewlines:
                    self.emitNewline()
                    self._suppressNewlines = True
                la = self._input.LA(1)
                if la not in [ord(' '), ord('\t'), ord('#')]:
                    self._suppressNewlines = False
                    self.emitFullDedent()

     

    def WHITESPACE_action(self, localctx , actionIndex):
        if actionIndex == 3:

            if (self._tokenStartColumn == 0 and self._openBRCount == 0
                and not self._lineContinuation):

                la = self._input.LA(1)
                if la not in [ord('\r'), ord('\n'), ord('#'), -1]:
                    self._suppressNewlines = False
                    wsCount = 0
                    for ch in self.text:
                        if   ch == ' ' : wsCount += 1
                        elif ch == '\t': wsCount += 8

                    if wsCount > self._indents.wsval():
                        self.emitIndent(len(self.text))
                        self._indents.push(wsCount)
                    else:
                        while wsCount < self._indents.wsval():
                            self.emitDedent()
                            self._indents.pop()
                        if wsCount != self._indents.wsval():
                            raise Exception()

     

    def OPEN_PAREN_action(self, localctx , actionIndex):
        if actionIndex == 4:
            self._openBRCount  += 1
     

    def CLOSE_PAREN_action(self, localctx , actionIndex):
        if actionIndex == 5:
            self._openBRCount  -= 1
     

    def OPEN_BRACE_action(self, localctx , actionIndex):
        if actionIndex == 6:
            self._openBRCount  += 1
     

    def CLOSE_BRACE_action(self, localctx , actionIndex):
        if actionIndex == 7:
            self._openBRCount  -= 1
     

    def OPEN_BRACKET_action(self, localctx , actionIndex):
        if actionIndex == 8:
            self._openBRCount  += 1
     

    def CLOSE_BRACKET_action(self, localctx , actionIndex):
        if actionIndex == 9:
            self._openBRCount  -= 1
     


